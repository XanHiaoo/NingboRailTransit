# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 22:32
# @Author  : Han
# @File    : 小功能.py
按钮下拉
button.menu = QMenu()#定义1个小的下拉菜单栏
 button.simple = QtWidgets.QAction("新建")
 button.hard = QtWidgets.QAction("删除")#定义“”新建“和“删除”两项
 button.menu.addAction(button.simple)
 button.menu.addAction(button.hard)#把两项加入到button中去
 button.setMenu(button.menu)
