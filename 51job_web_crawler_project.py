#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/10/14 9:06
# @Author  : Timber
# @Id      : 201950130527
# @File    : 51job_web_crawler_project.py
# @说明/注释: 
"""

import requests
import re

url = "https://search.51job.com/list/060000,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
headers = {
    "UserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}

response = requests.get(url, headers=headers).content.decode("gbk")

jobs = re.findall('"job_name":"(.*?)",', response)  # 职位
company_names = re.findall('"company_name":"(.*?)",', response)  # 公司名称
salaries = re.findall('"providesalary_text":"(.*?)",', response)  # 薪资
workareas = re.findall('"workarea_text":"(.*?)",', response)  # 工作区域
get_data = list(zip(jobs, company_names, salaries, workareas))

print(get_data)

f = open('王麒皓_201950130527_51job.txt', 'w')
for index in get_data:
    for i in index:
        f.write(i)
        f.write('   ')
    f.write('\n')
f.close()
