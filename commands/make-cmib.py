# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Lookup MIB
# ---------------------------------------------------------------------
# Copyright (C) 2007-2014 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import sys
import os
import logging
import datetime
import argparse
# NOC modules
from noc.core.management.base import BaseCommand
from noc.fm.models.mib import MIB
from noc.fm.models.mibdata import MIBData


logger = logging.getLogger("make-cmib")


class Command(BaseCommand):
    help = "Make compiled MIB for SA and PM scripts"

    def add_arguments(self, parser):
        parser.add_argument("-o", "--output",
                            dest="output", default="")
        parser.add_argument("args",
                            nargs=argparse.REMAINDER,)

    def handle(self, *args, **options):
        if len(args) != 1:
            self.stdout.write("Specify one MIB\n")
            self.die("")
        if options["output"]:
            self.prepare_dirs(options["output"])
            logging.debug("Opening file %s", options["output"])
            f = open(options["output"], "w")
        else:
            logging.debug("Dumping to stdout")
            f = sys.stdout
        mib = args[0]
        try:
            m = MIB.objects.get(name=mib)
        except MIB.DoesNotExist:
            self.stdout.write("MIB not found: %s\n" % mib)
            self.die("")
        year = datetime.date.today().year
        r = [
            "# -*- coding: utf-8 -*-",
            "# ----------------------------------------------------------------------",
            "# %s" % mib,
            "#     Compiled MIB",
            "#     Do not modify this file directly",
            "#     Run ./noc make-cmib instead",
            "# ----------------------------------------------------------------------",
            "# Copyright (C) 2007-%s The NOC Project" % year,
            "# See LICENSE for details",
            "# ----------------------------------------------------------------------",
            "",
            "# MIB Name",
            "NAME = \"%s\"" % mib,
            "# Metadata",
            "LAST_UPDATED = \"%s\"" %
            m.last_updated.isoformat().split("T")[0],
            "COMPILED = \"%s\"" % datetime.date.today().isoformat(),
            "# MIB Data: name -> oid",
            "MIB = {"
        ]
        rr = []
        for md in sorted(
                MIBData.objects.filter(mib=m.id),
                key=lambda x: [int(y) for y in x.oid.split(".")]
        ):
            rr += ["    \"%s\": \"%s\"" % (md.name, md.oid)]
        r += [",\n".join(rr)]
        r += ["}", ""]
        data = "\n".join(r)
        f.write(data)

    @staticmethod
    def prepare_dirs(path):
        d = os.path.dirname(path)
        if not os.path.isdir(d):
            logger.info("Creating directory %s", d)
            os.makedirs(d)

if __name__ == "__main__":
    Command().run()
