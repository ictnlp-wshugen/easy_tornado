# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/11/9 14:36
from threading import Thread

from typing import Callable


def deprecated(new_fn):
    """
    标记为弃用 decorator
    :param new_fn: 函数
    :return 包装函数
    """
    assert isinstance(new_fn, Callable)

    def function_wrapper(fn):
        assert isinstance(fn, Callable)

        def wrapper(*args, **kwargs):
            message = '{} will be deprecated in the future, ' \
                      'use {} instead'.format(fn.__name__, new_fn.__name__)
            from warnings import warn
            warn(message)
            fn(*args, **kwargs)

        return wrapper

    return function_wrapper


def async_call(fn):
    """
    异步调用 decorator
    :param fn: 函数
    :return 包装函数
    """
    assert isinstance(fn, Callable)

    def wrapper(*args, **kwargs):
        Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper
