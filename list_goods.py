#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/9/18 14:36
# @Author  : Timber
# @Id      : 201950130527
# @File    : list_goods.py
# @说明/注释: 
"""

products = [["iphone", 8000], ["honor", 6000], ["mi", 5000], ["tea", 200], ["Book", 100], ["奥利奥", 8]]
i = 0
length = len(products)

while i < length:
    print(i, products[i][0], products[i][1])
    i = i + 1

index = True
shopping = []

while index:
    choice = input("请输入要购买的商品编号:")
    if choice.isdigit():  # 判断是否为数字
        choice = int(choice)  # 强制类型转换
        if choice >= 0 and choice < length:
            shopping.append(products[choice])
            print("您已经添加了%s号商品到购物车" % products[choice])
        else:
            print("该商品不存在")

    elif choice == 'q':
        if len(shopping) > 0:
            print("-----您已经购买以下商品-----")
            for k, shop in enumerate(shopping):
                print("%s %s %s" % (k, shop[0], shop[1]))
        index = False
