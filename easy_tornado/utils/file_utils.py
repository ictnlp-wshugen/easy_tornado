# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
import hashlib
import json
import os
import shutil
import subprocess
import tempfile

from decorator import contextmanager

from ..functional import deprecated


# 文件绝对路径
def abspath(file_obj):
    return os.path.abspath(file_obj)


# 文件所在目录绝对路径
def absdir(file_obj):
    _abspath = abspath(file_obj)
    return os.path.dirname(_abspath)


# 路径父路径
def dirname(path):
    return os.path.dirname(path)


# 判断文件是否存在
def file_exists(_file):
    return os.path.exists(_file)


# 获取文件大小
def get_file_size(_file):
    return os.path.getsize(_file)


# 获取文件行数
def get_file_lines(_file):
    if not file_exists(_file):
        return -1
    lines = os.popen(r"wc -l %s | awk '{print $1}'" % _file).read()
    return int(lines)


# 移除文件
def remove_file(_file):
    shutil.rmtree(_file, ignore_errors=True)


# 准备目录
def create_if_not_exist_path(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)


# 拼接路径
def concat_path(base_path, sub_path):
    return os.path.join(base_path, sub_path)


cp = concat_path


# 拼接路径
@deprecated(new_fn=concat_path)
def format_path(base_path, sub_path):
    return concat_path(base_path, sub_path)


# 判断是否为绝对路径
def is_abspath(file_path):
    return file_path is not None and isinstance(file_path, str) and file_path.startswith('/')


# 修正路径(将holder中key对应的值增加base_path)
def refine_path(base_path, holder, key):
    if isinstance(holder, dict):
        assert key in holder
    elif isinstance(holder, list):
        assert isinstance(key, int) and 0 <= key < len(holder)
    else:
        raise TypeError('holder should be either dict or list, but got {}'.format(type(holder)))
    if is_abspath(holder[key]):
        return
    holder[key] = concat_path(base_path, holder[key])


def file_md5sum(file_path):
    """
    计算文件的MD5值
    :param file_path: 文件路径
    :return: 文件MD5
    """
    if not os.path.isfile(file_path):
        return
    ctx = hashlib.md5()
    with open(file_path, 'rb') as fp:
        while True:
            b = fp.read(8096)
            if not b:
                break
            ctx.update(b)
    return ctx.hexdigest()


# 追加文件
def append_to_file(_append_to_file_path, _append_from_file_path):
    if not file_exists(_append_to_file_path):
        cmd_create_str = 'cp %s %s' % (_append_from_file_path, _append_to_file_path)
        return not subprocess.call(cmd_create_str, shell=True)
    cmd_append_str = 'cat %s >> %s' % (_append_from_file_path, _append_to_file_path)
    return subprocess.call(cmd_append_str, shell=True) == 0


# 将pid写入文件pid
def write_pid(_pid_path):
    with open(_pid_path, 'w') as fp:
        fp.write(str(os.getpid()))


# 读取文件内容
def load_file_contents(_file_path):
    with open(_file_path, 'r') as fp:
        return fp.readlines()


# 向文件中写入一行
def write_line(_wfp, _line):
    if _wfp:
        _wfp.write(_line.strip())
        _wfp.write('\n')


# 写入内容至文件
def write_file_contents(file_path, contents):
    with open(file_path, 'w') as wfp:
        wfp.write(contents)


# 写入JSON内容
def write_json_contents(file_path, data):
    write_file_contents(file_path, json.dumps(data, ensure_ascii=True))


# 将可迭代的数据以行是的形式写入文件
def write_iterable_as_lines(file_path, iterable_obj, obj2line_func=lambda x: x):
    with open(file_path, 'w') as wfp:
        for obj in iterable_obj:
            write_line(wfp, obj2line_func(obj))


# 创建临时路径
@contextmanager
def mkdtemp():
    path = tempfile.mkdtemp()
    create_if_not_exist_path(path)
    yield path
    shutil.rmtree(path)
