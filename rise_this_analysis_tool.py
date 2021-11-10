#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
# @Time    : 2021/10/5 20:00
# @Author  : Timber
# @Id      : 201950130527
# @File    : rise_this_analysis_tool.py
# @说明/注释: 
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

full = pd.read_csv("table.csv")
cjxy = pd.read_csv("cjxy_t2.csv")

table = full.loc[:, ["毕业年级生计算机类", "Unnamed: 1"]].iloc[1:-1, :]

for col in table.columns:
    table[col] = table[col].apply(float)
table.set_index(table["毕业年级生计算机类"], inplace=True)
x_ticks = np.array(table["毕业年级生计算机类"])

plt.ylim([0, 25])
plt.hist(cjxy, color="blue", alpha=0.5)

plt.bar(x_ticks, table["Unnamed: 1"], color="red", alpha=0.5)
plt.xticks(range(0, len(x_ticks), 15))
plt.xlim([100, 300])

plt.show()

# for point in range(0,350,10):
#     table[float(point) < table["毕业年级生计算机类"].apply(float) <= float(point + 10), :]

# plt.bar(table["毕业年级生计算机类"], table["Unnamed: 1"])
# pct_labels = np.arange(0, 300, 15)
# plt.xticks(pct_labels)
# plt.show()
