# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
import json
import urllib
import six


# HTTP请求
def request(request_url, data=None, as_json=True):
    if data is None:
        data = {}
    _urllib = None
    if six.PY2:
        import urllib2
        _urllib = urllib2
    else:
        import urllib3
        _urllib = urllib3
    req = urllib3.Request(request_url)
    opener = urllib3.build_opener(urllib2.HTTPCookieProcessor())
    if as_json:
        response = opener.open(req, json.dumps(data, ensure_ascii=False))
    else:
        response = opener.open(req, urllib.urlencode(data))
    return response.read()
