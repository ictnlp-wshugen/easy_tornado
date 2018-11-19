# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
from .error_handler import error_exit
from ..compat import _happy_move_functions

_happy_move_functions(error_exit)
