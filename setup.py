#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 王树根
# email: wangshugen@ict.ac.cn
# date: 2018/8/23 14:29
from setuptools import setup, find_packages

setup(name='easy_tornado',
      version='0.5.1',
      description='A tornado based web framework package',
      author='empire (Wang Shugen)',
      author_email='wsg1107556314@163.com',
      url='https://lib.wshugen.cn/',
      packages=find_packages(),
      install_requires=['tornado', 'decorator', 'six', 'urllib3'])
