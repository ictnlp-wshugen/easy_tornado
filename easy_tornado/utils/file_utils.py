# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018年8月23日 14:26:49
import os
import subprocess


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
    os.system(r"rm -rf %s" % _file)


# 准备目录
def create_if_not_exist_path(target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)


# 格式化路径
def format_path(base_path, sub_path):
    return os.path.join(base_path, sub_path)


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
