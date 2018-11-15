# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/11/14 16:30
import io
import subprocess

from .utils.file_utils import write_file_contents

NOHUP = 'nohup'
BG_MARK = '&'


def shell_invoke(command, **kwargs):
    """
    Shell命令调用
    :param command: 命令
    :param kwargs: 关键字参数

    Args:
        log_prefix: 日志路径前缀
        debug: 是否为调试模式
        daemon: 是否在主线程退出之后仍然运行
    :return: 返回码
    """
    log_prefix = kwargs.pop('log_prefix', None)
    debug = kwargs.pop('debug', True)
    detach = kwargs.pop('detach', False)

    command = command.strip()
    if command == '' or command.startswith(NOHUP) or command.endswith(BG_MARK):
        raise ValueError('command should be a string not start with nohup and not end with &')

    stdout, stderr = None, None
    if log_prefix is not None:
        write_file_contents('{}.cmd'.format(log_prefix), command)
        stdout = io.open('{}.out'.format(log_prefix), mode='w', encoding='utf-8')
        stderr = stdout if debug else io.open('{}.err'.format(log_prefix), mode='w', encoding='utf-8')

    if detach:
        command = '{} {} {}'.format(NOHUP, command, BG_MARK)

    try:
        return subprocess.check_call(command, shell=True, stdout=stdout, stderr=stderr)
    except subprocess.CalledProcessError as e:
        return e.returncode


def python_invoke(command, **kwargs):
    """
    Python命令调用
    :param command: 命令
    :param kwargs: 关键字参数

    Args:
        version: Python版本号, 默认为2
        log_prefix: 日志路径前缀
        debug: 是否为调试模式
        daemon: 是否在主线程退出之后仍然运行
        python: Python命令
    :return: 返回码
    """
    command = command.strip()
    if command == '' or command.startswith('python'):
        raise ValueError('python command should be a string not start with python')

    python = kwargs.pop('python', None)
    if python is None:
        version = kwargs.pop('version', 2)
        if not (version == 2 or version == 3):
            raise ValueError('only support python2 and python3')
        python = 'python{}'.format(version)

    command = '{} -u {}'.format(python, command)
    return shell_invoke(command, **kwargs)
