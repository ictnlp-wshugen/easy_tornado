# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
from .validation import contain_keys
from .validation import in_range
from ..compat import _happy_move_functions

_happy_move_functions(contain_keys, in_range)
