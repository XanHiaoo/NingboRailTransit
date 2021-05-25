#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/20
# @Author : XIAO
# @File : newui.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QInputDialog,QDialog,QLineEdit)
from PyQt5.QtGui import QIcon
import sys
from utils import *
import beautify
class childwindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('&路线导航')
        self.resize(300, 200)
        startlabel = QLabel('&起始站', self)
        startline = QLineEdit(self)
        startlabel.setBuddy(startline)

        endlabel = QLabel('&终点站', self)
        endline = QLineEdit(self)
        endlabel.setBuddy(endline)

        btnstrat = QPushButton('&导航')
        btnCancel = QPushButton('&取消')
        btnstrat.setStyleSheet(beautify.qss)
        btnCancel.setStyleSheet(beautify.qss)
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(startlabel, 0, 0)
        mainLayout.addWidget(startline, 0, 1, 1, 2)

        mainLayout.addWidget(endlabel, 1, 0)
        mainLayout.addWidget(endline, 1, 1, 1, 2)

        mainLayout.addWidget(btnstrat, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        btnstrat.clicked.connect(lambda:self.start(startline,endline))
    def start(self,startline,endline):
        starts=startline.text()
        ends=endline.text()
        Navigation(starts, ends)

class mainwindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):

        # self.setFixedSize(self.width(), self.height());#不能放大
        self.setWindowTitle('宁波轨道交通')
        self.setWindowIcon(QIcon('yong.jpg'))
        self.resize(600,600)

        wwg = QWidget(self) # 全局控件（注意参数self），用于承载全局布局
        wlayout = QVBoxLayout(wwg)# 全局布局（注意参数wwg）

        vlayout1 = QHBoxLayout()#局部垂直布局1
        grid = QGridLayout()#局部网格布局
        vlayout2 = QHBoxLayout()  # 局部垂直布局2

        titlelabel=QLabel("宁波轨道交通查询乘车系统")
        # m_Pixmap = QPixmap("yong.jpg")
        # titlelabel.setPixmap(m_Pixmap)

        # 为局部布局添加控件
        vlayout1.addStretch(1)
        vlayout1.addWidget(titlelabel)
        vlayout1.addStretch(1)

        button_station=QPushButton("       站点查询       ")
        button_station.setStyleSheet(beautify.buttonstyle1)
        button_line=QPushButton("       线路查询       ")
        button_line.setStyleSheet(beautify.buttonstyle1)
        button_navi=QPushButton("       导航查询       ")
        button_navi.setStyleSheet(beautify.buttonstyle1)
        button_cardgenerate=QPushButton("      公交卡办理      ")
        button_cardgenerate.setStyleSheet(beautify.buttonstyle1)
        button_cardquery=QPushButton("      公交卡充值      ")
        button_cardquery.setStyleSheet(beautify.buttonstyle1)
        button_cardgo=QPushButton("      公交卡乘车      ")
        button_cardgo.setStyleSheet(beautify.buttonstyle1)
        grid.addWidget(QLabel(), 0, 0)
        grid.addWidget(button_station, 0,1)
        grid.addWidget(button_line, 1, 1)
        grid.addWidget(button_navi, 2, 1)
        grid.addWidget(QLabel(), 0, 2)
        grid.addWidget(button_cardgenerate, 0, 3)
        grid.addWidget(button_cardquery, 1, 3)
        grid.addWidget(button_cardgo, 2, 3)
        grid.addWidget(QLabel(), 0, 4)

        answerlabel=QLabel("   ...")
        answerlabel.setWordWrap(True)#label实现自动换行
        # answerlabel.setAlignment(QtCore.Qt.AlignTop)
        answerlabel.resize(200, 100)
        # vlayout2.addStretch(1)
        vlayout2.addWidget(answerlabel)
        # vlayout2.addStretch(1)


        # 在局部布局中添加控件，然后将其添加到全局布局中
        wlayout.addLayout(vlayout1)
        wlayout.addLayout(grid)
        wlayout.addLayout(vlayout2)

        self.setLayout(wlayout)#写这句保持相对布局
        button_station.clicked.connect(lambda:self.getstation(answerlabel))
        button_line.clicked.connect(lambda:self.getline(answerlabel))
        button_navi.clicked.connect(lambda:self.getnavi(answerlabel))
        # button_cardgenerate.clicked.connect(self.getstation)
        # button_cardquery.clicked.connect(self.getstation)
        # button_cardgo.clicked.connect(self.getstation)
        self.show()
    def getstation(self,label):
        txt, ok = QInputDialog.getText(self, '输入框', '输入查询站点')
        if ok and txt:
            l = Station_inquiry(txt)
            label.setText('通过'+txt+'的轨道交通线有:\n'+l)
    def getline(self,label):
        txt, ok = QInputDialog.getText(self, '输入框', '输入查询路线')
        if ok and txt:
            l = Line_inquiry(int(txt))
            s = strline(l)
        label.setText('轨道交通' + txt + '号线站点:\n' + s)
    def getnavi(self,label):
        console = childwindow()
        console.show()

        console.exec_()
        # lable.setText("1")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainwindow()
    # ax=childwindow()
    # ax.show()
    sys.exit(app.exec_())
