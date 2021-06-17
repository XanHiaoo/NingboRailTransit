#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/18 
# @Author : XIAO
# @File : testutils.py
from utils import *
import pandas as pd

# print(Navigation("南高教园区","长江路"))
# print(Navigation("南高教园区","宁波大学"))
# print(Navigation("南高教园区","舟孟北路"))
# print(Navigation("南高教园区","鼓楼"))
# print(GetAllrailline())
# print(Cardisexist(6))
# print(Cardquery('000001')[0][1])
#
dd=pd.read_csv('D:\\Users\\16030\\Desktop\\test.csv',header=None,encoding="gbk")
l=updateline(dd)
# l=updateline(1)
print(l)