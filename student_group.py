#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/9/15 17:02
# @Author  : Timber
# @Id      : 201950130527
# @File    : student_group.py
# @说明/注释: 
"""
import random

list_stu = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # 定义一个学生名单列表

# 通过随机数函数将列表打乱排序
random.shuffle(list_stu)

# 定义三个组
group = 3

# 分成gruop组
m = int(len(list_stu) / group)

# 每组成员
list_fz = []

# 创建分组列表
for i in range(1, len(list_stu), m):
    list_fz.append(list_stu[i:i + m])

print("分组列表为：", list_fz)

for i in range(len(list_fz)):
    print("第%d组名单:" % (i + 1), end=" ")
    for stu in list_fz[i]:
        print(stu, end=" ")
    print()
