#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/10/8 8:50
# @Author  : Timber
# @Id      : 201950130527
# @File    : request_get.py
# @说明/注释:
使用requests获取html内容
"""

import requests

url = "https://www.timberkito.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
}

req = requests.get(url=url, headers=headers)
print(req.text)
