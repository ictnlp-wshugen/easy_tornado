# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/11/6 14:05
from .monitoring import kill_process
from ..compat import _happy_move_functions

_happy_move_functions(kill_process)
