'''
FilePath: \Classes\Python\作业\requestGetDemo.py
Author: Liu Xingyu
WebSite: https://www.cnblogs.com/jaolvv
Date: 2021-10-01
Version: 1.0
Contact: 18423475135@163.com
Descripttion注释/说明: 使用requests获取html内容
'''
import requests


url = "https://www.timberkito.com"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38"
}

req = requests.get(url=url, headers=headers)
print(req.text)