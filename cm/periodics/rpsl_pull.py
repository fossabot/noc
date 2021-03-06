# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (C) 2007-2009 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------
"""
"""
import noc.lib.periodic

class Task(noc.lib.periodic.Task):
    name="cm.rpsl_pull"
    description=""

    def execute(self):
        from noc.cm.models import RPSL
        RPSL.global_pull()
        return True

