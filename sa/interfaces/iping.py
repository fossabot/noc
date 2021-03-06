# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------
# Copyright (C) 2007-2015 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------
"""
"""
from noc.core.interface.base import BaseInterface
from base import (IPParameter, DictParameter,
                  IntParameter, BooleanParameter, StringParameter, FloatParameter)


class IPing(BaseInterface):
    address = IPParameter()
    count = IntParameter(required=False)
    source_address = IPParameter(required=False)
    size = IntParameter(required=False)
    df = BooleanParameter(required=False)
    vrf = StringParameter(required=False)
    returns = DictParameter(attrs={
        "success": IntParameter(),
        "count": IntParameter(),
        "min": FloatParameter(required=False),
        "avg": FloatParameter(required=False),
        "max": FloatParameter(required=False)
    })
