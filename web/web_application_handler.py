# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
import json
import sys

from tornado.web import RequestHandler

sys.path.append('..')
from utils.time_utils import current_datetime


class WebApplicationHandler(RequestHandler):
    # 错误信息
    error_mapper = dict()
    none = 0
    error_mapper[none] = 'none'
    invalid_request = 1001
    error_mapper[invalid_request] = 'request param is invalid'
    not_found = 4004
    error_mapper[not_found] = 'not found'
    system_error = 5002
    error_mapper[system_error] = 'system error'

    # 调试选项
    debug = False

    # 后台进程
    daemon = False

    # 加载为json数据
    def load_request_data(self):
        try:
            params = json.loads(self.request.body)
            if self.debug:
                params['request_time'] = current_datetime()
                self.pretty_print(params)
        except ValueError:
            return False
        return params

    @staticmethod
    def pretty_print(data):
        print(json.dumps(data, ensure_ascii=False))

    def success_response(self, data=None):
        self.error_response(self.none, self.error_mapper[self.none], data)

    def error_response(self, error_no=invalid_request, error_desc=error_mapper[invalid_request], data=None):
        res = data
        if not data:
            res = dict()
        res['errno'] = error_no
        res['error'] = error_desc
        self.__json_response(res)

    def __json_response(self, data):
        if self.debug:
            data['response_time'] = current_datetime()
        self.__output_response(json.dumps(data, ensure_ascii=False))

    def __output_response(self, data):
        if self.debug:
            print(data)
        self.write(data)
        self.finish()

    def data_received(self, chunk):
        pass
