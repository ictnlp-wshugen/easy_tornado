# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
from .str_extension import md5sum
from .str_extension import parse_json
from ..compat import _happy_move_functions

_happy_move_functions(md5sum, parse_json)
