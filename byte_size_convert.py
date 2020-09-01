#!/usr/bin/python

from __future__ import absolute_import, division, print_function

from ansible.errors import AnsibleFilterError

import re


UNIT_VALUE = {
    'b': 0.125,
    'B': 1,
    'kB': 1000,
    'KiB': 1024,
    'MB': 1000**2,
    'MiB': 1024**2,
    'GB': 1000**3,
    'GiB': 1024**3,
    'TB': 1000**4,
    'TiB': 1024**4,
    'PB': 1000**5,
    'PiB': 1024**5,
    'EB': 1000**6,
    'EiB': 1024**6,
    'kb': 125,
    'mb': 125*1000**1,
    'gb': 125*1000**2,
    'tb': 125*1000**3,
    'pb': 125*1000**4,
    'eb': 125*1000**5,
    's': 512,
    'S': 4096,
}

UNIT_MAP = {
    '[kK]b': 'kb',
    '[kK]B': 'kB',
    '[kK]': 'KiB',
    '[mM]b': 'mb',
    '[mM]B': 'MB',
    '[mM]': 'MiB',
    '[gG]b': 'gb',
    '[gG]B': 'GB',
    '[gG]': 'GiB',
    '[tT]b': 'tb',
    '[tT]B': 'TB',
    '[tT]': 'TiB',
    '[pP]b': 'pb',
    '[pP]B': 'PB',
    '[pP]': 'PiB',
    '[eE]b': 'eb',
    '[eE]B': 'EB',
    '[eE]': 'EiB',
}


def byte_conversion(size, unit_in=None, unit_out="B"):

    def unit_parse(unit):
        if unit in UNIT_VALUE.keys():
            return unit
        for i in UNIT_MAP.keys():
            if re.match(i, unit):
                return UNIT_MAP[i]
        raise AnsibleFilterError("can't interpret the suffix: %s" % str(unit))

    m = re.match(r"(\d+\.?\d*)\s*([a-zA-Z]+)?", size)

    if m is None:
        raise AnsibleFilterError("can't interpret the input string: %s" % str(size))
    try:
        num = float(m.group(1))
    except Exception:
        raise AnsibleFilterError("can't interpret the number: %s" % str(m.group(1)))

    if unit_in is not None:
        unit_in = unit_parse(unit_in)
    elif m.group(2) is not None:
        unit_in = unit_parse(m.group(2))
    else:
        unit_in='B'

    unit_out = unit_parse(unit_out)

    convfactor = UNIT_VALUE[unit_in]/UNIT_VALUE[unit_out]
    result = num * convfactor

    return result



class FilterModule(object):
    def filters(self):
        return {
            'bc': byte_conversion,
        }
