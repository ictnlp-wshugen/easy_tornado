# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
from __future__ import print_function

import json

from .time_utils import Timer
from .web_utils import request


# 为非首行添加空格
def _add_indent(lines, space_cnt):
    s = lines.split('\n')
    # don't do anything for single-line stuff
    if len(s) == 1:
        return lines
    first = s.pop(0)
    s = [(space_cnt * ' ') + line for line in s]
    s = '\n'.join(s)
    s = first + '\n' + s
    return s


# 缩进打印
def print_indent(message):
    print(_add_indent(message, 2))


# 以某个消息为前缀打印
def print_prefix(subject, msg=''):
    if len(msg) != 0:
        subject = msg + ' ' + subject
    print(subject)


# 打印字典
def print_dict(data, msg=''):
    if len(msg) != 0:
        print(msg)
    for key in data:
        value = data[key]
        # 参数打印格式
        item = '%s => %s'
        print_indent(item % (key, value))


# 将字典以json格式打印
def print_dict_json(data_dict):
    print(json.dumps(data_dict, indent=2, sort_keys=True, ensure_ascii=False))


# 打印json
def print_json(json_string):
    print_dict_json(json.loads(json_string))


# Http API测试工具
class HttpTest(object):

    def __init__(self, url=None):
        self.url = url

    def set_url(self, host, context, port=80, https=False):
        schema = 'https' if https else 'http'
        self.url = '%s://%s:%d%s' % (schema, host, port, context)

    def request(self, uri, data=None, as_json=True):
        # 请求地址
        request_url = '%s%s' % (self.url, uri)
        print_prefix(request_url, "url:")

        # 请求数据
        if data is None:
            data = {}

        # 起始时间
        timer = Timer()
        timer.display_start("request at: ")

        # 打印请求数据
        print("request:")
        if len(data) != 0:
            print_dict_json(data)

        # 发起请求
        res = request(request_url, data, as_json)
        timer.finish()

        # 打印结果
        print("response:")
        print_json(res)

        # 结束时间
        timer.display_finish("finished at: ")
        print("time cost: %d s" % timer.cost())

        print()

        return res
