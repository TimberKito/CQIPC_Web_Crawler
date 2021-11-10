#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/10/19 15:58
# @Author  : Timber
# @Id      : 201950130527
# @File    : get_weather_website_graphics.py
# @说明/注释: bs4实现网页图片内容爬取
"""
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit  # BS内置库，用于推测文档编码
import urllib.request  # 发起请求，获取响应


def image_spider(start_url):
    global count  # 记录图片数量
    # 抓bug
    try:
        req = urllib.request.Request(start_url, headers=headers)  # 创建请求对象
        data = urllib.request.urlopen(req)  # 发起请求
        data = data.read()  # 获得响应体
        dammit = UnicodeDammit(data, ["utf-8", "gbk"])
        data = dammit.unicode_markup  # 解码
        # 指定Beautiful的解析器为 html.parser
        soup = BeautifulSoup(data, "html.parser")
        # 查找img标签
        images = soup.select("img")
        for image in images:
            # 抓bug
            try:
                src = image["src"]
                url = src
                count = count + 1
                # 调用download函数
                download(url, count)
            # 抓到bug的处理
            except Exception as err:
                print(err)
    except Exception as err:
        # 打印这个错误对象
        print(err)


def download(url, count):
    try:
        if url[len(url) - 4] == ".":  # 如果 图片url的长度的倒数第四位 = .
            ext = url[len(url) - 4:]
        else:
            ext = ".jpg"

        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=100)
        data = data.read()  # 读取文件
        # 以images+序号命名；wb表示以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，则覆盖写
        fobj = open("images" + str(count) + ext, "wb")
        fobj.write(data)  # 写入文件
        fobj.close()  # 关闭文件
        print("downloaded" + str(count) + ext)  # 打印下载(爬取)信息
    except Exception as err:
        print(err)


# 目标url
start_url = "http://www.weather.com.cn/weather/101280601.shtml"

# User-Agent会告诉网站服务器，访问者是通过什么工具来请求的
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"
}

count = 0

# 调用函数
image_spider(start_url)

print("The end...")
