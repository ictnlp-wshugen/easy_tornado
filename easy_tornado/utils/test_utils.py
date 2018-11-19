# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
from .http_test import HttpTest
from .http_test import print_dict
from .http_test import print_dict_json
from .http_test import print_function
from .http_test import print_indent
from .http_test import print_json
from .http_test import print_prefix
from ..compat import _happy_move_functions

_happy_move_functions(print_function, print_dict_json, print_dict, print_indent,
                      print_json, print_prefix, HttpTest)
