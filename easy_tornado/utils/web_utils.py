# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
import json
import urllib

import six


# 超时标记接口
class TimeoutError(Exception):
    pass


# HTTP请求
def request(request_url, data=None, as_json=True, timeout=None):
    if data is None:
        data = {}

    kwargs = dict()
    if timeout is not None:
        kwargs['timeout'] = timeout

    if six.PY2:
        import urllib2
        req = urllib2.Request(request_url)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        wrapped_data = json.dumps(data, ensure_ascii=False) if as_json else urllib.urlencode(data)
        # noinspection PyBroadException
        try:
            response = opener.open(req, wrapped_data, **kwargs)
        except Exception:
            raise TimeoutError
        result = response.read()
    else:
        import urllib3
        pool = urllib3.PoolManager()
        if as_json:
            kwargs['fields'] = data
        else:
            kwargs['body'] = urllib.urlencode(data)
        # noinspection PyBroadException
        try:
            response = pool.request('POST', request_url, **kwargs)
        except Exception:
            raise TimeoutError

        result = response.data
    return result
