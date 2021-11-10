#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/10/8 8:55
# @Author  : Timber
# @Id      : 201950130527
# @File    : urllib_get.py
# @说明/注释: 
"""

import urllib.request

url = 'https://www.timberkito.com'

response = urllib.request.urlopen(url)

print(response.read())
