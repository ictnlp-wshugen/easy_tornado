# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
import json
import urllib

import six
from urllib3.exceptions import ReadTimeoutError


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
        except URLError as e:
            if str(e.reason) == '[Errno 61] Connection refused':
                raise TimeoutError
        except StandardError as e:
            if e.message == 'timed out':
                raise TimeoutError
        result = response.read()
    else:
        from urllib3 import PoolManager
        from urllib3.exceptions import MaxRetryError
        from urllib3.exceptions import NewConnectionError

        pool = PoolManager()
        if data is not None:
            if as_json:
                kwargs['fields'] = data
            else:
                kwargs['body'] = urllib.urlencode(data)
        try:
            response = pool.request('POST', request_url, **kwargs)
        except MaxRetryError as e:
            if isinstance(e.reason, NewConnectionError):
                raise TimeoutError
        except ReadTimeoutError:
            raise TimeoutError
        result = response.data
    return result


if __name__ == '__main__':
    request('http://127.0.0.1:20181/wpynmt/instance/list.json', timeout=2)
