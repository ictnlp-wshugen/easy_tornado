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
    class StandardError(Exception):

        def __init__(self, *args, **kwargs):
            self._message = args[0]
            super(StandardError, self).__init__(*args, **kwargs)

        @property
        def message(self):
            return self._message


    C_StandardError = StandardError
    C_MAXINT = sys.maxsize


def utf8decode(text):
    return text.decode('utf-8') if six.PY2 else text


def utf8encode(text):
    return text.encode('utf-8') if six.PY2 else text