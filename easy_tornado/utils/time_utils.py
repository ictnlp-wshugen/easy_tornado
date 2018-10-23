# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
from __future__ import division

import time


# 获取当前时间戳
def current_timestamp():
    return time.time()


# 获取当前日期
def current_datetime(_timestamp=None):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(_timestamp))


# 获取当前时间戳对应的日期时间
def current_datetime_str(_timestamp=None):
    return time.strftime("%Y%m%d%H%M%S", time.localtime(_timestamp))


# 获取当前时间戳对应的日期时间
def current_datetime_str_s(_timestamp=None):
    return time.strftime("%Y%m%dT%H%M%S", time.localtime(_timestamp))


# 计时器类
class Timer(object):
    # 无效时间戳标志
    _invalid_ts = -1

    def __init__(self, debug=False):
        self.debug = debug
        self.start_ts = self._invalid_ts
        self.finish_ts = self._invalid_ts
        self.reset()

    def reset(self):
        self.start()
        if self.debug:
            self.display_start('start at: ')

    def start(self):
        self.start_ts = time.time()
        self.finish_ts = self._invalid_ts

    def finish(self):
        self.finish_ts = time.time()

    def cost(self):
        self._set_finish()
        return self.finish_ts - self.start_ts

    def display_start(self, msg):
        Timer._display_datetime(self.start_ts, msg)

    def display_finish(self, msg):
        self._set_finish()
        Timer._display_datetime(self.finish_ts, msg)

    def display_cost(self, msg=None):
        cost = self.cost()
        prefix = ''
        if msg:
            prefix = 'Job [%s] ' % msg
        self.display_start(prefix + 'start at: ')
        self.display_finish(prefix + 'finished at: ')
        print('cost %d seconds' % cost)

    def _set_finish(self):
        if self.finish_ts == self._invalid_ts:
            self.finish()

    @staticmethod
    def _display_datetime(_ts, _msg):
        _tmp_msg = current_datetime(_ts)
        if _msg:
            _tmp_msg = _msg + _tmp_msg
        print(_tmp_msg)
