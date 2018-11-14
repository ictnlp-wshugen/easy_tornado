# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/11/14 10:53
import six

C_StandardError = StandardError
if six.PY3:
    C_StandardError = BaseException
