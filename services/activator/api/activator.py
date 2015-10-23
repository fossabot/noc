# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Activator API
##----------------------------------------------------------------------
## Copyright (C) 2007-2015 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## NOC modules
from noc.core.service.api import API, APIError, api, executor
from noc.core.script.loader import loader


class ActivatorAPI(API):
    """
    Monitoring API
    """
    name = "activator"

    @api
    @executor("script")
    def script(self, name, credentials,
               capabilities=None,
               version=None,
               timeout=None):
        """
        Execute SA script
        :param name: Script name (with profile)
        :param credentials:
            Dict containing following fields
            * cli_protocol - CLI protocol (telnet, ssh)
            * address - IP address
            * cli_port (optional) - Non-standard CLI port
            * user (optional) - Login as user
            * password (optional) - User password
            * super_password (optional) - Enable password
            * snmp_version (optional) - Use SNMP version (None, v2c)
            * snmp_ro (optional) - Use SNMP R/O community
            * path (optional) - unstructured path
        :param capabilities: Dict of discovered capabilities
        :param version: Dict of discovered version
        :param timeout: Script timeout, in seconds
        """
        script_class = loader.get_script(name)
        if not script_class:
            raise APIError("Invalid script: %s" % name)
        script = script_class(
            credentials=credentials,
            capabilities=capabilities,
            version=version,
            timeout=timeout
        )
        result = script.run()
        return result
