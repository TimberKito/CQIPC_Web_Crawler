#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/9/29 16:02
# @Author  : Timber
# @Id      : 201950130527
# @File    : web_demo01.py
# @说明/注释: CQIPC_python爬虫课_课堂练习案例
"""
import requests

url = "www.timberkito.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31 "
}

response = requests.get(url, headers=headers)
print(response.text)
