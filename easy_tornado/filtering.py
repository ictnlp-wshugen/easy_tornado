# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/11/11 12:42


def filter_dict_object(data, *keys, **kwargs):
    """
    获取字典中想要/不要的键, 取决于kwargs参数
    :param data: 字典对象
    :param keys: 需要保留的键
    :param kwargs: 关键字参数
    :return 过滤掉的字典内容
    """
    if not isinstance(data, dict):
        raise TypeError('expected dict type, but got {}'.format(type(data)))
    result = dict()
    keep = False
    if 'keep' in kwargs and kwargs.pop('keep'):
        keep = True
    for key in data.keys():
        if keep:
            if key not in keys:
                result[key] = data.pop(key)
        else:
            if key in keys:
                result[key] = data.pop(key)
    return result


def filter_module_methods(module_name, filter_fn):
    """
    列出模块方法
    :param module_name: 模块名称
    :param filter_fn: 过滤函数 lambda 方法名: bool
    :return: 满足条件的方法列表
    """
    return list(filter(filter_fn, dir(module_name)))
