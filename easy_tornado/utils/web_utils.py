# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
import json
import urllib

import six


class TimeoutError(Exception):
    """
    # 超时标记接口
    """
    pass


# HTTP请求
def request(request_url, data=None, as_json=True, timeout=None):
    kwargs = dict()
    if timeout is not None:
        kwargs['timeout'] = timeout

    result = None
    if six.PY2:
        from urllib2 import Request
        from urllib2 import build_opener
        from urllib2 import HTTPCookieProcessor
        from urllib2 import URLError

        req = Request(request_url)
        opener = build_opener(HTTPCookieProcessor())
        if data is not None:
            data = json.dumps(data, ensure_ascii=False) if as_json else urllib.urlencode(data)
        try:
            response = opener.open(req, data, **kwargs)
            result = response.read()
        except URLError as e:
            # e.reason: 输出如，[Errno 61] Connection refused，但Mac和Unix的Errno不一样
            if str(e.reason).index('Connection refused'):
                raise TimeoutError
        except StandardError as e:
            if e.message == 'timed out':
                raise TimeoutError
    else:
        from urllib3 import PoolManager
        from urllib3.exceptions import MaxRetryError
        from urllib3.exceptions import NewConnectionError
        from urllib3.exceptions import ReadTimeoutError
        from urllib3.exceptions import RequestError

        pool = PoolManager()
        if data is not None:
            if as_json:
                kwargs['fields'] = data
            else:
                kwargs['body'] = urllib.urlencode(data)
        try:
            response = pool.request('POST', request_url, **kwargs)
            result = response.data
        except RequestError as e:
            if isinstance(e, MaxRetryError) and isinstance(e.reason, NewConnectionError):
                raise TimeoutError
            if isinstance(e, ReadTimeoutError):
                raise TimeoutError
    return result


if __name__ == '__main__':
    request('http://127.0.0.1:60001/controller.json', timeout=2)
