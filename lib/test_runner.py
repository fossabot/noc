# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Test code runner with Coverage
##----------------------------------------------------------------------
## Copyright (C) 2007-2010 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
import os
import unittest
import sys
import logging
import types
## Django modules
from django.utils import unittest  # unittest2 backport
from django.conf import settings
from django.test.utils import setup_test_environment, teardown_test_environment
from django.test import _doctest as doctest
from django.test.testcases import OutputChecker, DocTestRunner, TestCase
from django.core import management
from django.db import connection, connections
## Third-party modules
from coverage import coverage as Coverage
from south.logger import get_logger
import psycopg2
## NOC modules
from noc.lib import nosql


class ImportTestCase(unittest.TestCase):
    """
    Test there are no import errors with module
    """
    def __init__(self, module):
        super(ImportTestCase, self).__init__()
        self.module = module

    def __str__(self):
        return "<ImportTestCase: '%s'>" % self.module

    def runTest(self):
        __import__(self.module, {}, {}, "*")


class CoverageContext(object):
    """
    Coverage context manager
    """
    def __init__(self, runner, enable):
        self.runner = runner
        if enable:
            self.coverage = Coverage(config_file=False,
                                     source=self.runner.coverage_report)
            self.coverage.exclude(r"^\s*$")  # Exclude empty lines
            self.coverage.exclude(r"^\s*#.*$")  # Exclude comment blocks
            self.coverage.exclude(r"^\s*(import|from)\s")  # Exclude import statements
        else:
            self.coverage = None

    def info(self, message):
        logging.info(message)

    def __enter__(self):
        if self.coverage:
            self.info("Starting coverage")
            self.coverage.start()

    def __exit__(self, exc_type, exc_value, traceback):
        if self.coverage:
            self.info("Stopping coverage")
            self.coverage.stop()
            r_path = settings.COVERAGE_REPORT_PATH
            self.info("Writting coverage report to %s" % r_path)
            self.coverage.html_report(directory=r_path)


class DatabaseContext(object):
    """
    Database context manager
    """
    def __init__(self, parent, reuse=False, interactive=False, verbosity=1):
        self.parent = parent
        self.reuse = reuse
        self.autoclobber = not interactive
        self.verbosity = verbosity
        self.dbname = connection.settings_dict["NAME"]
        self.test_dbname = connection.creation._get_test_db_name()
        connection.creation.prepare_for_test_db_ddl = self._fixup

    def info(self, message):
        logging.info(message)

    def debug(self, message):
        logging.debug(message)

    def has_pg_db(self):
        """
        Check PosgreSQL test database already exists
        """
        dsn = ["dbname=%s" % self.test_dbname]
        if connection.settings_dict["USER"]:
            dsn += ["user=%s" % connection.settings_dict["USER"]]
        if connection.settings_dict["PASSWORD"]:
            dsn += ["password=%s" % connection.settings_dict["PASSWORD"]]
        dsn = " ".join(dsn)
        try:
            self.debug("Checking PostgreSQL database %s exists" % self.test_dbname)
            psycopg2.connect(dsn)
            self.debug("PostgreSQL database %s is already exists" % self.test_dbname)
            return True
        except psycopg2.OperationalError:
            return False

    def _fixup(self):
        # psycopg  2.4.2/Django 1.3.1 autocommit fixup
        # See https://code.djangoproject.com/ticket/16250 for details
        connection.connection.rollback()
        connection.connection.set_isolation_level(0)

    def __enter__(self):
        if self.reuse and self.has_pg_db():
            return
        self.info("Creating PostgreSQL test database")
        # Create PostgreSQL database
        connection.creation.create_test_db(self.verbosity,
                                           autoclobber=self.autoclobber)
        self.info("Creating MongoDB test database")
        # MongoDB
        nosql.create_test_db(self.verbosity, autoclobber=self.autoclobber)

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.reuse:
            # PostgreSQL
            self.info("Destroying PostgreSQL test database")
            connection.creation.destroy_test_db(self.dbname, self.verbosity)
            # MongoDB
            self.info("Destroying MongoDB test database")
            nosql.destroy_test_db(self.verbosity)


class TestEnvironmentContext(object):
    """
    Test environment context manager
    """
    def __enter__(self):
        # Save old settings
        self.old_is_test = settings.IS_TEST
        self.old_debug = settings.DEBUG
        # Temporary change settings
        settings.IS_TEST = True
        settings.DEBUG = False
        # Setup environment
        setup_test_environment()

    def __exit__(self, exc_type, exc_value, traceback):
        # Destroy test environment
        teardown_test_environment()
        # Restore settings
        settings.IS_TEST = self.old_is_test
        settings.DEBUG = self.old_debug


class TestRunner(object):
    """
    Testing engine
    """
    exclude_modules = ["noc.main.pyrules.", "noc.main.templates.", "noc.setup"]
    def __init__(self, test_labels, verbosity=1, interactive=True,
                 extra_tests=[], coverage=True, reuse_db=False):
        self.test_labels = test_labels
        self.verbosity = verbosity
        self.loglevel = logging.DEBUG if self.verbosity > 1 else logging.INFO
        self.interactive = interactive
        self.extra_tests = extra_tests
        self.enable_coverage = coverage
        self.reuse_db = reuse_db
        self.coverage_report = []  # List of files to report coverage

    def info(self, message):
        logging.info(message)

    def debug(self, message):
        logging.debug(message)

    def error(self, message):
        logging.error(message)

    def coverage(self, enable):
        """
        Get coverage context
        """
        return CoverageContext(self, enable=enable)

    def databases(self, reuse=False):
        """
        Get databases context
        """
        return DatabaseContext(self, reuse=reuse, interactive=self.interactive,
                               verbosity=self.verbosity)

    def test_environment(self):
        """
        Get test environment context
        """
        return TestEnvironmentContext()

    def get_manifest(self):
        """
        Generate a list of all python modules (file paths)
        """
        manifest = []
        # Root directory *.py
        manifest += [f for f in os.listdir(".")
                     if os.path.splitext(f)[1] == ".py" and f != "__init__.py"]
        dirs = (["lib", "tests"] +
                [app[4:] for app in settings.INSTALLED_APPS
                 if app.startswith("noc.")])
        for top in dirs:
            for root, dirs, files in os.walk(top):
                parts = root.split(os.sep)
                if len(parts) > 1 and parts[1] in ("migrations", "management"):
                    continue
                manifest += [os.path.join(root, f) for f in files
                             if (not f.startswith(".") and
                                os.path.splitext(f)[1] == ".py")]
        return manifest

    def get_modules(self, test_labels):
        """
        Get modules for test suite
        """
        def path_to_mod(path):
            """
            >>> path_to_mod("lib/test_runner.py")
            'noc.lib.test_runner'
            >>> path_to_mod("sa/profiles/__init__.py")
            'noc.sa.profiles'
            """
            if os.path.splitext(path)[1] == ".py":
                path = path[:-3]
            m = ["noc"] + path.split(os.path.sep)
            if m[-1] == "__init__":
                m = m[:-1]
            return ".".join(m)
            
        def mod_to_path(mod):
            """
            >>> mod_to_path("noc.lib.test_runner")
            'lib/test_runner.py'
            >>> mod_to_path("noc.sa.profiles")
            'sa/profiles/__init__.py'
            """
            if mod.startswith("noc."):
                mod = mod[4:]
            path = mod.replace(".", os.path.sep)
            if os.path.isdir(path):
                path = os.path.join(path, "__init__")
            return path + ".py"

        def is_match(module, labels):
            """ Check module matches test label """
            parts = module.split(".")
            lp = len(parts)
            for l in labels:
                ll = len(l)
                if lp >= ll and parts[:ll] == l:
                    return True
            return False

        def to_exclude(module):
            for x in self.exclude_modules:
                if module.startswith(x):
                    return True
            return False

        # Build files manifest
        manifest = [path_to_mod(p) for p in self.get_manifest()]
        if test_labels:
            # Filter modules
            l = [tl.split(".") for tl in test_labels]
            manifest = [m for m in manifest if is_match(m, l)]
        # Exclude modules
        manifest = [m for m in manifest if not to_exclude(m)]
        # Coverate report manifest
        self.coverage_report = [mod_to_path(m) for m in manifest]
        # Get unittests and modules
        tests = [f for f in manifest if "tests" in f.split(".")[:-1]]
        st = set(tests)
        modules = [f for f in manifest if f not in st]
        n_unittests = len(tests)
        n_mods = len(modules)
        self.info("Found modules: %d unittests, %d python" % (
            n_unittests, n_mods))
        return modules, tests

    def get_suite(self, modules, tests):
        # Prepare suite
        suite = unittest.TestSuite()
        # Add import tests
        suite.addTests([ImportTestCase(m) for m in modules])
        # Add doctests
        output_checker = OutputChecker()
        for m in modules:
            try:
                suite.addTests(doctest.DocTestSuite(m, checker=output_checker,
                                                    runner=DocTestRunner))
            except ValueError:
                # No tests
                continue
        # Add unittests
        for m in tests:
            try:
                mo = __import__(m, {}, {}, "*")
            except (ImportError, AssertionError):
                suite.addTest(ImportTestCase(m))
                continue
            t = []
            for name in dir(mo):
                obj = getattr(mo, name)
                if (isinstance(obj, (type, types.ClassType)) and
                    issubclass(obj, unittest.TestCase)):
                    if obj.__module__ == m:
                        t += [unittest.defaultTestLoader.loadTestsFromTestCase(obj)]
            suite.addTest(unittest.TestSuite(t))
        self.info("Test suite build: %d test cases are found" % suite.countTestCases())
        return suite

    def run(self):
        """
        Set up environment and run tests.
        Returns number of errors
        """
        # Set up south logger
        get_logger().setLevel(self.loglevel)
        # Set up system logger
        logging.basicConfig(level=logging.DEBUG,
                            format="%(asctime)s %(message)s")
        # Prepare environment and run tests
        with self.test_environment():
            # Get test suite
            modules, tests = self.get_modules(self.test_labels)
            # Check modules are found
            if len(modules) == 0 and len(tests) == 0:
                self.info("No modules to test. Exiting")
                return 0
            # Run test suite in database and coverage context
            with self.coverage(enable=self.enable_coverage):
                with self.databases(reuse=self.reuse_db):
                    # Initialize database: Wrap as tests
                    management.call_command("sync-perm")
                    #management.call_command("sync-pyrules")
                    #management.call_command("sync-collections")
                    # Add as tests
                    suite = self.get_suite(modules, tests)
                    self.info("Running test suite")
                    runner = unittest.TextTestRunner(verbosity=self.verbosity)
                    result = runner.run(suite)
                    self.info("Test suite completed")
        # Return summary
        return len(result.failures) + len(result.errors)
