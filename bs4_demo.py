#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/9/29 16:58
# @Author  : Timber
# @Id      : 201950130527
# @File    : bs4_demo.py
# @说明/注释: 
"""

from bs4 import BeautifulSoup

f = open("baidu.html","rb")

html = f.read()

bs = BeautifulSoup(html,"html.parser")

print(bs.title)