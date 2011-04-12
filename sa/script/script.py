# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Service Activation Script classes
##----------------------------------------------------------------------
## Copyright (C) 2007-2011 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from __future__ import with_statement
import threading
import thread
import re
import logging
import time
import sys
import Queue
import cPickle
import ctypes
import datetime
##
## NOC modules
from noc.sa.protocols.sae_pb2 import TELNET, SSH, HTTP
from noc.lib.registry import Registry
from noc.sa.profiles import profile_registry
from noc.lib.debug import format_frames, get_traceback_frames
from noc.sa.script.exception import *
from noc.sa.script.telnet import CLITelnetSocket
from noc.sa.script.ssh import CLISSHSocket
from noc.sa.script.http import HTTPProvider
from noc.sa.script.snmp import SNMPProvider

##
## Script.scripts proxy hub
##
class ScriptProxy(object):
    ##
    ## Constructor
    ##      parent - Script instance
    ##
    def __init__(self, parent):
        self._parent=parent
    
    ##
    ## Return ScriptCallProxy instance for script 'name'
    ##
    def __getattr__(self, name):
        return ScriptCallProxy(self._parent, self._parent.profile.scripts[name])
    
    ##
    ## Check profile has script name
    ##
    def has_script(self, name):
        return self._parent.profile.scripts.has_key(name)

##
## Script call wrapper to mimic script run with simple function call
##
class ScriptCallProxy(object):
    ##
    ##
    ##
    def __init__(self, parent, script):
        self.parent=parent
        self.script=script
    
    ##
    ## Call script
    ##
    def __call__(self, **kwargs):
        s=self.script(self.parent.profile, self.parent.activator, self.parent.access_profile, parent=self.parent, **kwargs)
        return s.guarded_run()
    

##
## Script regustry
##
class ScriptRegistry(Registry):
    name="ScriptRegistry"
    subdir="profiles"
    classname="Script"
    apps=["noc.sa"]
    exclude=["highlight"]
    
    ##
    ## Register generic scripts to all supporting profiles
    ##
    def register_generics(self):
        generics=[]
        for c in [c for c in self.classes.values() if c.name and c.name.startswith("Generic.")]:
            g, name=c.name.split(".")
            for p in profile_registry.classes:
                s_name=p+"."+name
                # Do not register generic when specific exists
                if s_name in self.classes:
                    continue
                to_register=True
                for r_name, r_interface in c.requires:
                    rs_name=p+"."+r_name
                    if rs_name not in self.classes or not self.classes[rs_name].implements_interface(r_interface):
                        to_register=False
                        break
                if to_register:
                    self.classes[s_name]=c
                    profile_registry[p].scripts[name]=c
                    generics+=[s_name]
        logging.debug("Registering generics: %s"%", ".join(sorted(generics)))
    
    ##
    ## Register all scripts and generic scripts
    ##
    def register_all(self):
        super(ScriptRegistry, self).register_all()
        self.register_generics()
    

script_registry=ScriptRegistry()

##
## Metaclass for script
##
_execute_chain=[]
class ScriptBase(type):
    def __new__(cls, name,bases,attrs):
        global _execute_chain
        m=type.__new__(cls, name,bases,attrs)
        m._execute_chain=_execute_chain
        _execute_chain=[]
        m.implements=[c() for c in m.implements]
        script_registry.register(m.name, m)
        if m.name and not m.name.startswith("Generic."):
            pv, pos,sn=m.name.split(".",2)
            profile_registry["%s.%s"%(pv, pos)].scripts[sn]=m
        return m


##
## Configuration context manager to use with "with" statement
##
class ConfigurationContextManager(object):
    def __init__(self, script):
        self.script=script
    
    ##
    ## Entering context
    ##
    def __enter__(self):
        self.script.enter_config()
    
    ##
    ## Leaving context
    ##
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.script.leave_config()
        else:
            raise exc_type, exc_val
    

##
## Mark cancelable part of script
##
class CancellableContextManager(object):
    def __init__(self, script):
        self.script=script
    
    ##
    ## Entering context
    ##
    def __enter__(self):
        self.script.is_cancelable=True
    
    ##
    ## Leaving context
    ##
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_cancelable=False
    

##
## Silently ignore specific exceptions
##
class IgnoredExceptionsContextManager(object):
    def __init__(self, iterable):
        self.exceptions=set(iterable)
    
    ##
    ## Entering context
    ##
    def __enter__(self):
        pass
    
    ##
    ## Leaving context
    ##
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type and exc_type in self.exceptions:
            return True # Supress exception
    

##
## Service activation script
##
class Script(threading.Thread):
    __metaclass__=ScriptBase
    name=None
    description=None
    # Enable call cache
    # If True, script result will be cached and reused
    # during lifetime of parent script
    cache=False
    # Interfaces list. Each element of list must be Interface subclass
    implements=[]
    # Scripts required by generic script.
    # For common scripts - empty list
    # For generics - list of pairs (script_name, interface)
    requires=[]
    # Constants
    TELNET=TELNET
    SSH=SSH
    HTTP=HTTP
    TIMEOUT=120 # 2min by default
    #
    LoginError=LoginError
    CLISyntaxError=CLISyntaxError
    NotSupportedError=NotSupportedError
    UnexpectedResultError=UnexpectedResultError
    #
    _execute_chain=[]

    def __init__(self, profile, activator, access_profile, timeout=0, parent=None, **kwargs):
        self.start_time=time.time()
        self.parent=parent
        self.access_profile=access_profile
        self.attrs={}
        self._timeout=timeout if timeout else self.TIMEOUT
        if self.access_profile.address:
            p=self.access_profile.address
        elif self.access_profile.path:
            p=self.access_profile.path
        else:
            p="<unknown>"
        self.debug_name="script-%s-%s"%(p, self.name)
        self.encoding = None # Device encoding. None if UTF8
        for a in access_profile.attrs:
            self.attrs[a.key]=a.value
            # Try to get encoding from attributes
            if a.key == "encoding":
                v = a.value.strip()
                # Test encoding
                try:
                    u"test".encode(v)
                    self.encoding = v
                    self.debug("Using '%s' encoding" % v)
                except LookupError:
                    self.error("Unknown encoding: '%s'" % v)
        super(Script, self).__init__(name=self.debug_name, kwargs=kwargs)
        self.activator=activator
        self.servers=activator.servers
        self.profile=profile
        self.cli_provider=None
        self.http=HTTPProvider(self.access_profile)
        self.snmp=SNMPProvider(self)
        self.status=False
        self.result=None
        self.call_cache={} # Suitable only when self.parent is None. Cached results for scripts marked with "cache"
        self.error_traceback=None
        self.login_error=None
        self.strip_echo=True
        self.kwargs=kwargs
        self.scripts=ScriptProxy(self)
        self.need_to_save=False
        self.to_disable_pager=not self.parent and self.profile.command_disable_pager
        self.log_cli_sessions_path=None # Path to log CLI session
        self.is_cancelable=False # Can script be cancelled
        self.e_timeout=False # Script terminated with timeout
        self.e_cancel=False # Scrcipt cancelled
        self.e_not_supported=False # NotSupportedError risen
        self._thread_id=None # Python 2.5 compatibility
        # Set up CLI session logging
        if self.parent:
            self.log_cli_sessions_path=self.parent.log_cli_sessions_path
        elif self.activator.log_cli_sessions\
            and self.activator.log_cli_sessions_ip_re.search(self.access_profile.address)\
            and self.activator.log_cli_sessions_script_re.search(self.name):
            self.log_cli_sessions_path=self.activator.log_cli_sessions_path
            for k, v in [
                ("ip", self.access_profile.address),
                ("script", self.name),
                ("ts", datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))]:
                self.log_cli_sessions_path=self.log_cli_sessions_path.replace("{{%s}}"%k, v)
            self.cli_debug("IP: %s SCRIPT: %s"%(self.access_profile.address, self.name),"!")
    
    ##
    ## Compile arguments into version check function
    ## Returns callable accepting self and version hash arguments
    ##
    @classmethod
    def compile_match_filter(cls, *args, **kwargs):
        c=[lambda self, x, g=f: g(x) for f in args]
        for k, v in kwargs.items():
            # Split to field name and lookup operator
            if "__" in k:
                f, o=k.split("__")
            else:
                f=k
                o="exact"
            # Check field name
            if f not in ("vendor", "platform", "version", "image"):
                raise Exception("Invalid field '%s'"%f)
            # Compile lookup functions
            if o=="exact":
                c+=[lambda self, x,f=f,v=v: x[f]==v]
            elif o=="iexact":
                c+=[lambda self, x,f=f,v=v: x[f].lower()==v.lower()]
            elif o=="startswith":
                c+=[lambda self, x,f=f,v=v: x[f].startswith(v)]
            elif o=="istartswith":
                c+=[lambda self, x,f=f,v=v: x[f].lower().startswith(v.lower())]
            elif o=="endswith":
                c+=[lambda self, x,f=f,v=v: x[f].endswith(v)]
            elif o=="iendswith":
                c+=[lambda self, x,f=f,v=v: x[f].lower().endswith(v.lower())]
            elif o=="contains":
                c+=[lambda self, x,f=f,v=v: v in x[f]]
            elif o=="icontains":
                c+=[lambda self, x,f=f,v=v: v.lower() in x[f].lower()]
            elif o=="in":
                c+=[lambda self, x,f=f,v=v: x[f] in v]
            elif o=="regex":
                c+=[lambda self, x,f=f,v=re.compile(v): v.search(x[f]) is not None]
            elif o=="iregex":
                c+=[lambda self, x,f=f,v=re.compile(v, re.IGNORECASE): v.search(x[f]) is not None]
            elif o=="isempty": # Empty string or null
                c+=[lambda self, x,f=f,v=v: not x[f] if v else x[f]]
            elif f=="version":
                if o=="lt": # <
                    c+=[lambda self, x,v=v: self.profile.cmp_version(x["version"], v)<0 ]
                elif o=="lte": # <=
                    c+=[lambda self, x,v=v: self.profile.cmp_version(x["version"], v)<=0 ]
                elif o=="gt": # >
                    c+=[lambda self, x,v=v: self.profile.cmp_version(x["version"], v)>0 ]
                elif o=="gte": # >=
                    c+=[lambda self, x,v=v: self.profile.cmp_version(x["version"], v)>=0 ]
                else:
                    raise Exception("Invalid lookup operation: %s"%o)
            else:
                raise Exception("Invalid lookup operation: %s"%o)
        # Combine expressions into single lambda
        return reduce(lambda x, y: lambda self, v,x=x,y=y: x(self, v) and y(self, v), c, lambda self, x: True)
    
    ##
    ## execute method decorator
    ##
    @classmethod
    def match(cls, *args, **kwargs):
        def decorate(f):
            global _execute_chain
            # Append to the execute chain
            _execute_chain+=[(x, f)]
            return f
        # Compile check function
        x=cls.compile_match_filter(*args, **kwargs)
        # Return decorated function
        return decorate
    
    ##
    ## inline version for Script.match
    ##
    def match_version(self, *args, **kwargs):
        return self.compile_match_filter(*args, **kwargs)(self, self.scripts.get_version())
    
    ##
    ##
    ##
    def cli_debug(self, msg, chars=None):
        if not self.log_cli_sessions_path:
            return
        m=datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
        if chars:
            m+=chars*50
        m+="\n"
        m+=msg+"\n"
        with open(self.log_cli_sessions_path, "a") as f:
            f.write(m)
    
    ##
    ## Checks script is stale and must be terminated
    ##
    def is_stale(self):
        return time.time()-self.start_time > self._timeout
    
    ##
    ## Check script implements interface
    ##
    @classmethod
    def implements_interface(cls, interface):
        for i in cls.implements:
            if type(i)==interface:
                return True
        return False
    
    ##
    ## Debug log message
    ##
    def debug(self, msg):
        logging.debug(u"[%s] %s"%(self.debug_name, unicode(str(msg), "utf8")))
    
    ##
    ## Error log message
    ##
    def error(self, msg):
        logging.error(u"[%s] %s"%(self.debug_name, unicode(str(msg), "utf8")))
    
    ##
    ## Return root script
    ##
    @property
    def root(self):
        if self.parent:
            return self.parent.root
        else:
            return self
    
    ##
    ## Get cached result or raise KeyError
    ##
    def get_cache(self, key1, key2):
        s=self.root
        return s.call_cache[repr(key1)][repr(key2)]
    
    ##
    ## Set cached result
    ##
    def set_cache(self, key1, key2, value):
        key1=repr(key1)
        key2=repr(key2)
        s=self.root
        if key1 not in s.call_cache:
            s.call_cache[key1]={}
        s.call_cache[key1][key2]=value
    
    ##
    ## Wrap around script call with all possible checkings
    ##
    def guarded_run(self):
        # Enforce interface type checking
        for i in self.implements:
            self.kwargs=i.script_clean_input(self.profile, **self.kwargs)
        self.debug("Running script: %s (%s)"%(self.name, self.kwargs))
        # Use cached result when available
        if self.cache and self.parent is not None:
            try:
                result=self.get_cache(self.name, self.kwargs)
                self.debug("Script returns with cached result: %s"%result)
                return result
            except KeyError:
                self.debug("Not in call cache: %s, %s"%(self.name, self.kwargs))
                pass
        # Calling script body
        self._thread_id=thread.get_ident()
        result=self.execute(**self.kwargs)
        # Enforce interface result checking
        for i in self.implements:
            result=i.script_clean_result(self.profile, result)
        # Cache result when required
        if self.cache and self.parent is not None:
            self.debug("Write to call cache: %s, %s, %s"%(self.name, self.kwargs,result))
            self.set_cache(self.name, self.kwargs,result)
        self.debug("Script returns with result: %s"%result)
        return result
    
    ##
    ## Serialize script results
    ##
    def serialize_result(self, result):
        return cPickle.dumps(result)
    
    ##
    ## Script thread worker method
    ##
    def run(self):
        self.debug("Running")
        result=None
        try:
            with self.cancelable():
                result=self.guarded_run()
        except TimeOutError:
            self.error("Timed out")
            self.e_timeout=True
        except CancelledError:
            self.error("Cancelled")
            self.e_cancel=True
        except self.NotSupportedError:
            self.e_not_supported=True
        except self.LoginError, why:
            self.login_error=why.args[0]
            self.error("Login failed: %s"%self.login_error)
        except:
            if self.e_cancel:
                # Race condition caught. Handle CancelledError
                self.error("Cancelled")
            else:
                t, v,tb=sys.exc_info()
                r=[str(t), str(v)]
                r+=[format_frames(get_traceback_frames(tb))]
                self.error_traceback="\n".join(r)
                self.debug("Script traceback:\n%s"%self.error_traceback)
        else:
            # Serialize result
            self.result=self.serialize_result(result)
            if self.parent is None and self.need_to_save and self.profile.command_save_config:
                self.debug("Saving config")
                self.cli(self.profile.command_save_config)
            # Exit sequence
            if self.parent is None and self.cli_provider is not None and self.profile.command_exit:
                self.debug("Exiting")
                self.cli_provider.submit(self.profile.command_exit)
        self.debug("Closing")
        if self.activator.to_save_output and result:
            self.activator.save_result(result, self.motd)
        if self.cli_provider:
            self.activator.request_call(self.cli_provider.close, flush=True)
        if self.snmp:
            self.snmp.close()
        self.activator.on_script_exit(self)
    
    ##
    ## Default script behavior:
    ## Pass through _execute_chain and call appropriative handler
    ##
    def execute(self, **kwargs):
        if self._execute_chain and not self.name.endswith(".get_version"):
            # Get version information
            v=self.scripts.get_version()
            # Find and execute proper handler
            for c, f in self._execute_chain:
                if c(self, v):
                    return f(self, **kwargs)
            # Raise error 
            raise NotSupportedError()
    
    ##
    ## Request CLI provider's queue
    ## Handle cancel condition
    ##
    def cli_queue_get(self):
        while True:
            try:
                return self.cli_provider.queue.get(block=True, timeout=1)
            except Queue.Empty:
                pass
            except thread.error:
                # Bug in python's Queue module:
                # Sometimes, tries to release unacquired lock
                time.sleep(1)
    
    ##
    ## Run CLI provider if not available
    ##
    def request_cli_provider(self):
        if self.parent:
            self.cli_provider=self.parent.request_cli_provider()
        elif self.cli_provider is None:
            self.debug("Running new provider")
            if self.access_profile.scheme==self.TELNET:
                s_class=CLITelnetSocket
            elif self.access_profile.scheme==self.SSH:
                s_class=CLISSHSocket
            else:
                raise UnknownAccessScheme(self.access_profile.scheme)
            self.cli_provider=s_class(self.activator.factory, self.profile, self.access_profile) #@todo: pass activator
            self.cli_queue_get()
            self.debug("CLI Provider is ready")
            # Set up session when necessary
            if self.profile.setup_session:
                self.debug("Setting up session")
                self.profile.setup_session(self)
            # Disable pager when necessary
            if self.to_disable_pager:
                self.debug("Disable paging")
                self.to_disable_pager=False
                self.cli(self.profile.command_disable_pager)
        return self.cli_provider
    
    ##
    ## Execute CLI command and return a result
    ## if list_re is None, return a string
    ## if list_re is regular expression object, return a list of dicts (group name -> value), one dict per matched line
    ##
    def cli(self, cmd, command_submit=None, bulk_lines=None, list_re=None):
        #
        self.debug("cli(%s)"%cmd)
        self.cli_debug(cmd, ">")
        # Submit command
        command_submit=self.profile.command_submit if command_submit is None else command_submit
        if self.activator.use_canned_session:
            data=self.activator.cli(cmd)
        else:
            self.request_cli_provider()
            self.cli_provider.submit(cmd, command_submit=command_submit, bulk_lines=bulk_lines)
            data=self.cli_queue_get()
        # Encode to UTF8 if requested
        if self.encoding:
            data = unicode(data, self.encoding).encode("utf8")
        # Save canned output if requested
        if self.activator.to_save_output:
            self.activator.save_interaction("cli", cmd, data)
        if isinstance(data, Exception):
            # Exception captured
            raise data
        # Check for syntax error
        if self.profile.pattern_syntax_error and re.search(self.profile.pattern_syntax_error, data):
            raise self.CLISyntaxError()
        # Echo cancelation
        if self.strip_echo and data.lstrip().startswith(cmd):
            data=data.lstrip()
            if data.startswith(cmd+"\n"):
                # Remove first line
                data=self.strip_first_lines(data.lstrip())
            else:
                # Some switches, like ProCurve do not send \n after the echo
                data=data[len(cmd):]
        # Convert to list when required
        if list_re:
            r=[]
            for l in data.splitlines():
                match=list_re.match(l.strip())
                if match:
                    r+=[match.groupdict()]
            data=r
        self.debug("cli(%s) returns:\n---------\n%s\n---------"%(cmd, repr(data)))
        self.cli_debug(data, "<")
        return data
    
    ##
    ## Clean up config from all unnecessary trash
    ##
    def cleaned_config(self, config):
        return self.profile.cleaned_config(config)
    
    ##
    ## Strip first lines
    ##
    def strip_first_lines(self, text, lines=1):
        t=text.split("\n")
        if len(t)<=lines:
            return ""
        else:
            return "\n".join(t[lines:])
    
    ##
    ## Expand expressions like "1, 2,5-7" to [1, 2,5,6,7]
    ##
    def expand_rangelist(self, s):
        result={}
        for x in s.split(","):
            x=x.strip()
            if x=="":
                continue
            if "-" in x:
                l, r=[int(y) for y in x.split("-")]
                if l>r:
                    x=r
                    r=l
                    l=x
                for i in range(l, r+1):
                    result[i]=None
            else:
                result[int(x)]=None
        return sorted(result.keys())
    
    ##
    ## Convert a 6-octet string to MAC address
    ##
    def hexstring_to_mac(self, s):
        return ":".join(["%02X"%ord(x) for x in s])
    
    ##
    ## Cancel script
    ##
    def cancel_script(self):
        # Can cancel only inside guarded_run
        if not self.is_cancelable:
            self.error("Cannot cancel non-cancelable scipt")
            return
        if not self.isAlive():
            self.error("Trying to kill already dead thread")
            return
        if not self._thread_id:
            self.error("Cannot cancel the script without thread_id")
            return
        # Raise CancelledError in script's thread
        self.e_cancel=True
        r=ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self._thread_id), ctypes.py_object(CancelledError))
        if r==1:
            self.debug("Cancel event sent")
            # Remote exception raised.
            if self.cli_provider:
                # Awake script thread if waiting for CLI
                self.cli_provider.queue.put(None)
                self.cli_provider.queue.put(None)
        elif r>1:
            # Failed to raise exception
            # Revert back thread state
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self.ident), None)
            self.error("Failed to cancel script")
    
    ##
    ## Debugging helper to hang the script
    ##
    def hang(self):
        logging.debug("Hanging script")
        e=threading.Event()
        while True:
            e.wait(1)
    
    ##
    ## Returns configuration context
    ##
    def configure(self):
        return ConfigurationContextManager(self)
    
    ##
    ## Return cancelable context
    ##
    def cancelable(self):
        return CancellableContextManager(self)
    
    ##
    ## Return ignorable exceptions context
    ##
    def ignored_exceptions(self, iterable):
        return IgnoredExceptionsContextManager(iterable)
    
    ##
    ## Enter configuration mote
    ##
    def enter_config(self):
        if self.profile.command_enter_config:
            self.cli(self.profile.command_enter_config)
    
    ##
    ## Leave configuration mode
    ##
    def leave_config(self):
        if self.profile.command_leave_config:
            self.cli(self.profile.command_leave_config)
            self.cli("") # Guardian empty command to wait until configuration is finally written
    
    ##
    ## Save current config
    ##
    def save_config(self, immediately=False):
        if immediately:
            if self.profile.command_save_config:
                self.cli(self.profile.command_save_config)
        else:
            self.schedule_to_save()
    
    ##
    ##
    ##
    def schedule_to_save(self):
        self.need_to_save=True
        if self.parent:
            self.parent.schedule_to_save()
    
    ##
    ## Return message of the day
    ##
    @property
    def motd(self):
        if self.activator.use_canned_session:
            return self.activator.get_motd()
        if not self.cli_provider:
            self.request_cli_provider()
        return self.cli_provider.motd
    
    ##
    ## Match s against regular expression rx using re.search
    ## Raise UnexpectedResultError if regular expression is not matched.
    ## Returns match object.
    ## rx can be string or compiled regular expression
    ##
    def re_search(self, rx, s, flags=0):
        if isinstance(rx, basestring):
            rx=re.compile(rx, flags)
        match=rx.search(s)
        if match is None:
            raise self.UnexpectedResultError()
        return match
    
    ##
    ## Match s against regular expression rx using re.match
    ## Raise UnexpectedResultError if regular expression is not matched.
    ## Returns match object.
    ## rx can be string or compiled regular expression
    ##
    def re_match(self, rx, s, flags=0):
        if isinstance(rx, basestring):
            rx=re.compile(rx, flags)
        match=rx.match(s)
        if match is None:
            raise self.UnexpectedResultError()
        return match
    
    ##
    ## Find first matching regular expression
    ## or raise Unexpected result error
    ##
    def find_re(self, iter, s):
        for r in iter:
            if r.search(s):
                return r
        raise self.UnexpectedResultError()
    
    ##
    ## Return scheme id by string name
    ##
    @classmethod
    def get_scheme_id(self, scheme):
        try:
            return {
                "telnet" : TELNET,
                "ssh"    : SSH,
                "http"   : HTTP,
            }[scheme]
        except KeyError:
            raise UnknownAccessScheme(scheme)
    
