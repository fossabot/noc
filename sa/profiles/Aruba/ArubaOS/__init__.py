# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Vendor: Aruba
# OS:     ArubaOS
# ---------------------------------------------------------------------
# Copyright (C) 2007-2015 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import re
# NOC modules
from noc.core.profile.base import BaseProfile


class Profile(BaseProfile):
    name = "Aruba.ArubaOS"
    pattern_unprivileged_prompt = r"^(?P<hostname>\S+)\s*>"
    pattern_prompt = r"^(?P<hostname>\S+)\s*#"
    pattern_syntax_error = r"% Parse error"
    command_super = "enable"
    pattern_more = [
        (r"--More-- \(q\) quit \(u\) pageup \(/\) search \(n\) repeat", " ")
    ]
    rogue_chars = [
        re.compile(r"\r\s+\r"),
        "\r"
    ]
