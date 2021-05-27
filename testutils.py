#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/18 
# @Author : XIAO
# @File : testutils.py
from utils import *
# l=Station_inquiry('慈城')
# print(l)
# s=Navigation1('儿童公园', '樱花公园')
# print(s)
# s=getalllinename()
# print(s[1])
l=Line_inquiry(3)
for i in range(0,len(l)):
    print(l[i])