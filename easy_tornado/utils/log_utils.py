# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/10/30 14:29
import sys


def _add_indent(lines, space_cnt):
    """
    add blank before message

    :param lines: lines to be operated
    :type lines: Iterable of str

    :param space_cnt: space number
    :type space_cnt: int

    :return: lines with each started with space_cnt blanks
    """
    s = lines.split('\n')
    # don't do anything for single-line stuff
    if len(s) == 1:
        return lines
    first = s.pop(0)
    s = [(space_cnt * ' ') + line for line in s]
    s = '\n'.join(s)
    s = first + '\n' + s
    return s


def it_print(message, indent=0, device=1, newline=True):
    """
    in time print: print message to console immediately

    :param message: the message to be printed
    :type message: object

    :param indent: number of blank to be indented, default 0
    :type indent: int

    :param device: stdout -> 1, stderr -> 2, default 1
    :type device: int

    :param newline: whether to append a new line, default True
    :type newline: bool
    """
    if not isinstance(message, list) and isinstance(message, tuple):
        message = [message]

    message = _add_indent(message, indent)

    if device == 2:
        device = sys.stderr
    else:
        device = sys.stdout

    device.writelines(message)
    if newline:
        device.write('\n')
    device.flush()
