# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/11/19 11:03
from .logging import it_print
from ..functional import deprecated


def exit_print(*args, **kwargs):
    """
    print message and exit
    :param args: see it_print
    :param kwargs: see it_print
    """
    if 'device' not in kwargs:
        kwargs['device'] = 2
    it_print(*args, **kwargs)
    errno = kwargs.pop('errno', 0)
    exit(int(errno))


@deprecated(new_fn=exit_print)
def error_exit(errno=0, error=None):
    """
    print message and exit
    :param errno: error code
    :param error: error message
    """
    if error is not None:
        it_print(error)
    exit(errno)
