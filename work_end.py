#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/11/4 19:46
# @Author  : Timber
# @Id      : 201950130527
# @File    : work_end.py
# @说明/注释: 
"""

# 是专门用于解析xml语言的库
from lxml import etree
import urllib.request


def img(start_url):
    global count
    try:
        # 定义一个请求对象
        req = urllib.request.Request(start_url, headers=headers)
        # 发送请求，获取请求对象，得到服务器响应
        data = urllib.request.urlopen(req)
        # 获取网页源码
        data = data.read()
        # 通过xpath爬取内容
        re_xpath = etree.HTML(data)  # 将html转变为树形结构，类型为lxml.etree
        # 提取所有img下的src属性值
        images = re_xpath.xpath('//img/@src')
        print('test1', images)
        return
        # dammit = UnicodeDammit(data,["utf-8","gbk"])
        # # 将data进行解码
        # data = dammit.unicode_markup
        # # 指定bs4的解析器为html.parser
        # soup = BeautifulSoup(data,"html.parser")
        # # 获取网页中图片的路径
        # images=soup.select("img")
        # # 遍历images当中的每一个img标签
        for image in images:
            try:
                src = image["src"]
                url = src
                count = count + 1
                download(url, count)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)


def download(url, count):
    try:
        # 判断倒数第四位是否为.
        if (url[len(url) - 4] == "."):
            # 留下图片的后缀
            ext = url[len(url) - 4:]
        else:
            # 后缀修改为jpg
            ext = ".jpg"
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req, timeout=100)
        data = data.read()
        # 打开images存储图片
        fobj = open("images\\" + str(count) + ext, "wb")
        fobj.write(data)
        fobj.close()
        print("downloaded" + str(count) + ext)
    except Exception as err:
        print(err)


start_url = "http://www.weather.com.cn/weather/101280601.shtml"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}
count = 0
img(start_url)
print("The End")
