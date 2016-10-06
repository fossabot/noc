# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## Clickhouse query engine
##----------------------------------------------------------------------
## Copyright (C) 2007-2016 The NOC Project
## See LICENSE for details
##----------------------------------------------------------------------

## Python modules
from collections import namedtuple
## Third-party modules
import six


class OP(object):
    def __init__(self, min=None, max=None, join=None,
                 prefix=None, convert=None, function=None):
        self.min = min
        self.max = max
        self.join = join
        self.prefix = prefix
        self.convert = convert
        self.function = function

    def to_sql(self, seq):
        l = len(seq)
        if self.min and l < self.min:
            raise ValueError("Missed argument: %s" % seq)
        if self.max and l > self.max:
            raise ValueError("Too many arguments: %s" % seq)
        if self.convert:
            return self.convert(seq)
        else:
            r = ["(%s)" % to_sql(x) for x in seq]
            if self.join:
                r = self.join.join(r)
            elif self.function:
                r = "%s(%s)" % (self.function, ", ".join(r))
            else:
                r = r[0]
            if self.prefix:
                r = "%s%s" % (self.prefix, r)
            return r


OP_MAP = {
    # Comparison
    "$eq": OP(min=2, max=2, join=" = "),
    "$gt": OP(min=2, max=2, join=" > "),
    "$gte": OP(min=2, max=2, join=" >= "),
    "$lt": OP(min=2, max=2, join=" < "),
    "$lte": OP(min=2, max=2, join=" <= "),
    "$ne": OP(min=2, max=2, join=" != "),
    "$like": OP(min=2, max=2, join=" LIKE "),
    # @todo: a?b:c
    # Logical
    "$and": OP(min=1, join=" AND "),
    "$or": OP(min=1, join=" OR "),
    "$xor": OP(min=1, join=" XOR "),
    # Unary
    "$field": OP(min=1, max=1, convert=lambda x: escape_field(x[0])),
    "$neg": OP(min=1, max=1, prefix="-"),
    # Arithmetic
    "$plus": OP(min=2, max=2, join=" + "),
    "$minus": OP(min=2, max=2, join=" - "),
    "$mult": OP(min=2, max=2, join=" * "),
    "$div": OP(min=2, max=2, join=" / "),
    "$mod": OP(min=2, max=2, join=" % "),
    # Functions
    "$abs": OP(min=1, max=1, function="ABS"),
    "$now": OP(min=0, max=0, function="NOW"),
    # today
    # lower
    # upper
    # substring
    # Aggregate functions
    "$count": OP(min=0, max=0, function="COUNT"),
    "$any": OP(min=1, max=1, function="ANY"),
    "$anylast": OP(min=1, max=1, function="ANYLAST"),
    "$min": OP(min=1, max=1, function="MIN"),
    "$max": OP(min=1, max=1, function="MAX"),
    "$sum": OP(min=1, max=1, function="SUM"),
    "$avg": OP(min=1, max=1, function="AVG"),
    "$uniq": OP(min=1, max=1, function="UNIQ"),
    "$median": OP(min=1, max=1, function="MEDIAN")
}


def escape_str(s):
    return "%s" % s


def escape_field(s):
    return "%s" % s


def to_sql(expr):
    """
    Convert query expression to sql
    :param expr:
    :return:
    """
    if type(expr) == dict:
        for k in expr:
            op = OP_MAP.get(k)
            if not op:
                raise ValueError("Invalid operator: %s" % expr)
            v = expr[k]
            if type(v) != list:
                v = [v]
            return op.to_sql(v)
    elif isinstance(expr, six.string_types):
        return "\'%s\'" % escape_str(expr)
    elif isinstance(expr, six.integer_types):
        return str(expr)
    elif isinstance(expr, float):
        return str(expr)