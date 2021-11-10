'''
FilePath: \Classes\Python\作业\requestPostDemo.py
Author: Liu Xingyu
WebSite: https://www.cnblogs.com/jaolvv
Date: 2021-10-01
Version: 1.0
Contact: 18423475135@163.com
Descripttion注释/说明: 
'''
import requests

url = "https://www.cnblogs.com/jaolvv"

headers = {
    "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

response = requests.post(url, headers=headers)
print(response.text)