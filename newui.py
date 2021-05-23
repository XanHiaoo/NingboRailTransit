#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/20
# @Author : XIAO
# @File : newui.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5. QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
from utils import *

class mainwindow(QMainWindow):
    def __init__(self):
        super(mainwindow,self).__init__()
        self.initUI()
    def initUI(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局


        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件
        self.setWindowTitle('宁波轨道交通查询乘车系统')
        self.setWindowIcon(QIcon('yong.jpg'))
        self.centralwidget.setObjectName("centralwidget")
        self.lbltitle = QtWidgets.QLabel(self.centralwidget)
        # _translate = QtCore.QCoreApplication.translate
        # self.label.setText(_translate("MainWindow", "宁波轨道交通乘车查询系统"))

if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = mainwindow()
    ex.initUI()
    ex.show()
    sys.exit(app.exec_())