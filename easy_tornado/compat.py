# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/11/14 10:53
import sys

import six

if six.PY2:
    C_StandardError = StandardError
    C_MAXINT = sys.maxint
if six.PY3:
    C_StandardError = BaseException
    C_MAXINT = sys.maxsize
