#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/9/13 14:07
# @Author  : Timber
# @Id      : 201950130527
# @File    : grading_judgment_method.py
# @说明/注释: 
"""


def grades():
    score = float(input("Enter your score:"))
    if score > 100:
        print("You score is error!")
    elif 100 >= score >= 90:
        level = "A"
        print("Your score level is:" + level + "!")
    elif 90 > score >= 80:
        level = "B"
        print("Your score level is:" + level + "!")
    elif 80 > score >= 70:
        level = "C"
        print("Your score level is:" + level + "!")
    elif 70 > score >= 60:
        level = "D"
        print("Your score level is:" + level + "!")
    elif 60 > score >= 0:
        level = "E"
        print("Your score level is:" + level + "!")
    elif score < 0:
        print("Your score is error!")


grades()
