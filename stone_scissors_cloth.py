#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/9/14 16:10
# @Author  : Timber
# @Id      : 201950130527
# @File    : stone_scissors_cloth.py
# @说明/注释: 
"""

import random


def little_game():
    try:
        Computer = random.randint(1, 3)
        player = input("1.剪刀 2.石头 3.布\t请输入对应编号:")
        player = int(player)
        arr = ["剪刀", "石头", "布"]
        print("电脑出的:" + arr[Computer - 1] + "\t玩家出的:" + arr[player - 1])
        if Computer == player:
            print("平局")
        elif (Computer == 1 and player == 3) or (Computer == 2 and player == 1) or (Computer == 3 and player == 2):
            print("电脑胜")
        else:
            print("玩家胜")
    except Exception:
        print("非法字符！请输入对应编号:1.剪刀 2.石头 3.布")
        little_game()


little_game()
