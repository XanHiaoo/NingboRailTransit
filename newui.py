#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/20
# @Author : XIAO
# @File : newui.py
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QWidget, QGridLayout,QTextEdit,
                             QPushButton, QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QInputDialog,QDialog,QLineEdit,QComboBox,QFileDialog)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import sys
from utils import *
import beautify
import webbrowser
from PyQt5.QtWebEngineWidgets import QWebEngineView
import win32api 

'''导航界面'''
class childwindownavi(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('路线导航')
        self.setWindowIcon(QIcon('Icon/yong.jpg'))
        self.resize(900,900)
        palette = QPalette()
        pix = QtGui.QPixmap('Icon/linepic.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(QPixmap(pix)))
        self.setPalette(palette)

        self.startcomboline = QComboBox()
        self.endcomboline = QComboBox()
        self.startcombosation = QComboBox()
        self.endcombostation = QComboBox()
        self.startcomboline.setStyleSheet(beautify.QComboBoxstyle1)
        self.startcombosation.setStyleSheet(beautify.QComboBoxstyle1)
        self.endcomboline.setStyleSheet(beautify.QComboBoxstyle1)
        self.endcombostation.setStyleSheet(beautify.QComboBoxstyle1)

        allline=getalllinename()#获得所有路线
        for line in allline:
            self.startcomboline.addItem(line)
            self.endcomboline.addItem(line)

        self.startcomboline.currentTextChanged.connect(self.updatestartcombosation1)
        self.endcomboline.currentTextChanged.connect(self.updatestartcombosation2)

        startlabel = QLabel('    &起始站:', self)
        startlabel.setBuddy(self.startcomboline)
        startlabel.setStyleSheet(beautify.labelstyle1)

        endlabel = QLabel('    &终点站:', self)
        endlabel.setBuddy(self.endcomboline)
        endlabel.setStyleSheet(beautify.labelstyle1)

        btnstrat = QPushButton('&导航')
        btnCancel = QPushButton('&取消')
        btnstrat.setStyleSheet(beautify.buttonstyle1)
        btnCancel.setStyleSheet(beautify.buttonstyle1)
        self.navilabel=QLabel("   ...")
        self.navilabel.setWordWrap(True)
        self.navilabel.setStyleSheet(beautify.labelstyle3)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(startlabel, 0, 0)
        mainLayout.addWidget(self.startcomboline, 0, 1 )
        mainLayout.addWidget(self.startcombosation, 0, 2)

        mainLayout.addWidget(endlabel, 1, 0)
        mainLayout.addWidget(self.endcomboline, 1, 1)
        mainLayout.addWidget(self.endcombostation, 1, 2)

        mainLayout.addWidget(btnstrat, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        mainLayout.addWidget(self.navilabel,3,0,1,3)

        btnstrat.clicked.connect(self.start)
    def start(self):
        starts=self.startcombosation.currentText()
        ends=self.endcombostation.currentText()
        if(starts=='' or ends==''):
            self.navilabel.setText("请同时选择起始站和终点站")
            return
        s=''
        Navigation(starts, ends)
        nowline=0
        for way in utilsnaviway:
            if way[1]!=nowline and way[1]!=0:
                nowline=way[1]
                s+=way[0]+'(轨道交通'+str(nowline)+'号线)'+'->  '
        s+=ends
        self.navilabel.setText(s)

    def updatestartcombosation1(self):
        self.startcombosation.clear()
        s=self.startcomboline.currentText()
        dict = GetLineNameToId()
        l = Line_inquiry(int(dict[s]))
        for i in range(0, len(l)):
            self.startcombosation.addItem(l[i])

    def updatestartcombosation2(self):
        self.endcombostation.clear()
        s=self.endcomboline.currentText()
        dict = GetLineNameToId()
        l = Line_inquiry(int(dict[s]))
        for i in range(0, len(l)):
            self.endcombostation.addItem(l[i])

'''乘车界面'''
class childwindowtake(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('乘车系统')
        self.setWindowIcon(QIcon('Icon/yong.jpg'))
        self.resize(900,900)
        palette = QPalette()
        pix = QtGui.QPixmap('Icon/linepic.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(QPixmap(pix)))
        self.setPalette(palette)

        self.cardid = QLineEdit()
        self.cardid.setMaxLength(6)
        self.startcomboline = QComboBox()
        self.endcomboline = QComboBox()
        self.startcombosation = QComboBox()
        self.endcombostation = QComboBox()
        self.startcomboline.setStyleSheet(beautify.QComboBoxstyle1)
        self.startcombosation.setStyleSheet(beautify.QComboBoxstyle1)
        self.endcomboline.setStyleSheet(beautify.QComboBoxstyle1)
        self.endcombostation.setStyleSheet(beautify.QComboBoxstyle1)

        allline=getalllinename()#获得所有路线
        for line in allline:
            self.startcomboline.addItem(line)
            self.endcomboline.addItem(line)

        self.startcomboline.currentTextChanged.connect(self.updatestartcombosation1)
        self.endcomboline.currentTextChanged.connect(self.updatestartcombosation2)

        cardidlabel = QLabel('    &卡号:', self)
        cardidlabel.setBuddy(self.cardid)
        cardidlabel.setStyleSheet(beautify.labelstyle1)

        startlabel = QLabel('    &起始站:', self)
        startlabel.setBuddy(self.startcomboline)
        startlabel.setStyleSheet(beautify.labelstyle1)

        endlabel = QLabel('    &终点站:', self)
        endlabel.setBuddy(self.endcomboline)
        endlabel.setStyleSheet(beautify.labelstyle1)

        btnstrat = QPushButton('&开始乘车')
        btnCancel = QPushButton('&取消')
        btnstrat.setStyleSheet(beautify.buttonstyle1)
        btnCancel.setStyleSheet(beautify.buttonstyle1)
        self.navilabel=QLabel("   ...")
        self.navilabel.setWordWrap(True)
        self.navilabel.setStyleSheet(beautify.labelstyle3)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(cardidlabel,0,0)
        mainLayout.addWidget(self.cardid, 0, 1)
        mainLayout.addWidget(startlabel, 1, 0)
        mainLayout.addWidget(self.startcomboline, 1, 1 )
        mainLayout.addWidget(self.startcombosation, 1, 2)
        mainLayout.addWidget(endlabel, 2, 0)
        mainLayout.addWidget(self.endcomboline, 2, 1)
        mainLayout.addWidget(self.endcombostation, 2, 2)

        mainLayout.addWidget(btnstrat, 3, 1)
        mainLayout.addWidget(btnCancel, 3, 2)

        mainLayout.addWidget(self.navilabel,4,0,1,3)



        btnstrat.clicked.connect(self.start)
    def start(self):
        cardnum=self.cardid.text()
        if(Cardisexist(cardnum)==False):
            self.navilabel.setText("请输入正确的公交卡号")
            return
        starts=self.startcombosation.currentText()
        ends=self.endcombostation.currentText()
        if(starts=='' or ends==''):
            self.navilabel.setText("请同时选择起始站和终点站")
            return
        Navigation(starts, ends)
        waylen=len(utilsnaviway)-1
        infor=Cardquery(cardnum)
        s = ''
        flag=False
        balance=infor[0][1]
        cost=0
        if(infor[0][0]==1):
            cost=waylen*0.5
            if(cost>balance):
                s+='公交卡余额不足'
            else:
                s = starts + '->' + ends + '（共' + str(waylen) + '站）\n扣费:' + str(waylen * 0.5) + '\n余额：'+str(infor[0][1]-waylen * 0.5)
                balance-=cost
                flag=True

        elif (infor[0][0] == 2):
            cost = waylen * 0.3
            if(cost>balance):
                s += '公交卡余额不足'
            else:
                s = starts + '->' + ends + '（共' + str(waylen) + '站）\n学生卡扣费:' + str(waylen * 0.3) + '\n余额：' + str(infor[0][1] - waylen * 0.3)
                balance -= cost
                flag = True
        elif (infor[0][0] == 3):
                s = starts + '->' + ends + '（共' + str(waylen) + '站）\n老人卡免费乘坐'
                flag = True

        if(flag):
            UpdateCardRecord(cardnum,balance,cost,starts,ends)
        self.navilabel.setText(s)

    def updatestartcombosation1(self):
        self.startcombosation.clear()
        s=self.startcomboline.currentText()
        dict = GetLineNameToId()
        l = Line_inquiry(int(dict[s]))
        for i in range(0, len(l)):
            self.startcombosation.addItem(l[i])

    def updatestartcombosation2(self):
        self.endcombostation.clear()
        s=self.endcomboline.currentText()
        dict = GetLineNameToId()
        l = Line_inquiry(int(dict[s]))
        for i in range(0, len(l)):
            self.endcombostation.addItem(l[i])

'''路线管理界面'''
class filewindow(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.flag=False
        self.filename=''
        self.setWindowTitle('轨道路线管理系统')
        self.setWindowIcon(QIcon('Icon/yong.jpg'))
        self.resize(600, 600)
        palette = QPalette()
        pix = QtGui.QPixmap('Icon/linepic.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(QPixmap(pix)))
        self.setPalette(palette)
        okButton = QPushButton("选择文件")
        okButton.setStyleSheet(beautify.buttonstyle1)
        addButton = QPushButton("确认修改")
        addButton.setStyleSheet(beautify.buttonstyle1)
        self.textEdit=QTextEdit()
        hbox = QHBoxLayout()
        hbox1=QHBoxLayout()
        hbox.addWidget(self.textEdit)
        hbox1.addStretch(1)
        hbox1.addWidget(okButton)
        hbox1.addWidget(addButton)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox1)
        self.setLayout(vbox)

        okButton.clicked.connect(self.showDialog)
        addButton.clicked.connect(self.addline)


    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\Users\\16030\\Desktop')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                self.filename=fname[0]
                data = f.read()
                self.textEdit.setText(data)
                self.flag=True
    def addline(self):
        if(self.flag):
            dd = pd.read_csv(self.filename, header=None, encoding="gbk")
            updateline(dd)
            self.textEdit.setText('路线修改成功')
        else:
            self.textEdit.setText('请选择文件')

'''主界面'''
class mainwindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def initUI(self):
        # QDesktopServices.openUrl(QUrl("user1/User1.html"))
        # browser = QWebEngineView()
        # browser.load(QUrl("user1/User1.html"))
        # browser.show()
        # self.setFixedSize(self.width(), self.height());#不能放大
        self.setWindowTitle('宁波轨道交通')
        self.setWindowIcon(QIcon('Icon/yong.jpg'))
        self.resize(900,900)
        palette = QPalette()
        pix = QtGui.QPixmap('Icon/linepic.jpg')
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(QPixmap(pix)))
        self.setPalette(palette)
        # self.setWindowOpacity(0.8)

        #设置图标
        symbollbl = QLabel(self)
        pixmap = QPixmap("Icon/biaozhi.png")
        pixmap = pixmap.scaled(100, 100)
        symbollbl.setPixmap(pixmap)

        wwg = QWidget(self) # 全局控件（注意参数self），用于承载全局布局
        wlayout = QVBoxLayout(wwg)# 全局布局（注意参数wwg）

        vlayout1 = QHBoxLayout()#局部水平布局1
        grid = QGridLayout()#局部网格布局
        vlayout2 = QHBoxLayout()  # 局部垂直布局2

        titlelabel=QLabel("宁波轨道交通查询乘车系统\n     Ningbo Rail Transit")
        titlelabel.setStyleSheet(beautify.labelstyle2)
        # m_Pixmap = QPixmap("Icon/yong.jpg")
        # titlelabel.setPixmap(m_Pixmap)

        # 为局部布局添加控件
        vlayout1.addStretch(1)
        vlayout1.addWidget(symbollbl)
        # vlayout1.addStretch(1)
        vlayout1.addWidget(titlelabel)
        vlayout1.addStretch(1)


        button_station=QPushButton("       站点查询       ")
        button_station.setStyleSheet(beautify.buttonstyle1)
        button_line=QPushButton("       线路查询       ")
        button_line.setStyleSheet(beautify.buttonstyle1)
        button_navi=QPushButton("       导航查询       ")
        button_navi.setStyleSheet(beautify.buttonstyle1)
        button_cardtakeway=QPushButton("      公交卡乘车      ")
        button_cardtakeway.setStyleSheet(beautify.buttonstyle1)
        button_cardmanage=QPushButton("      公交卡管理      ")
        button_cardmanage.setStyleSheet(beautify.buttonstyle1)
        button_linemanage=QPushButton("      轨道路线管理      ")
        button_linemanage.setStyleSheet(beautify.buttonstyle1)
        # grid.addWidget(QLabel(), 0, 0)
        grid.addWidget(button_station, 0,1)
        grid.addWidget(button_line, 1, 1)
        grid.addWidget(button_navi, 2, 1)
        # grid.addWidget(QLabel(), 0, 2)
        grid.addWidget(button_cardtakeway, 0, 3)
        grid.addWidget(button_cardmanage, 1, 3)
        grid.addWidget(button_linemanage, 2, 3)
        # grid.addWidget(QLabel(), 0, 4)

        self.answerlabel=QLabel("   ...")
        self.answerlabel.setStyleSheet(beautify.labelstyle3)
        self.answerlabel.setWordWrap(True)#label实现自动换行
        # self.answerlabel.setAlignment(QtCore.Qt.AlignTop)
        self.answerlabel.resize(200, 100)
        # vlayout2.addStretch(1)
        vlayout2.addWidget(self.answerlabel)
        # vlayout2.addStretch(1)


        # 在局部布局中添加控件，然后将其添加到全局布局中
        wlayout.addLayout(vlayout1)
        # wlayout.addStretch(1)
        wlayout.addLayout(grid)
        # wlayout.addStretch(1)
        wlayout.addLayout(vlayout2)

        self.setLayout(wlayout)#写这句保持相对布局
        button_station.clicked.connect(self.getstation)
        button_line.clicked.connect(self.getline)
        button_navi.clicked.connect(self.getnavi)
        button_cardtakeway.clicked.connect(self.takeway)
        button_cardmanage.clicked.connect(self.cardexe)
        button_linemanage.clicked.connect(self.linemanage)
        self.show()
    def getstation(self):
        txt, ok = QInputDialog.getText(self, '输入框', '输入查询站点')
        if ok and txt:
            l = Station_inquiry(txt)
            self.answerlabel.setText('通过'+txt+'的轨道交通线有:\n'+l)

    def getline(self):
        items=getalllinename()
        dict=GetLineNameToId()
        item, okPressed = QInputDialog.getItem(self, "Get item", "线路:", items, 0, False)
        if okPressed and item:
            l = Line_inquiry(int(dict[item]))
            s = strline(l)
            self.answerlabel.setText(item + '站点:\n' + s)

    def getnavi(self):
        console = childwindownavi()
        console.show()
        console.exec_()
        # lable.setText("1")

    def takeway(self):
        console = childwindowtake()
        console.show()
        console.exec_()

    def linemanage(self):
        console = filewindow()
        console.show()
        console.exec_()

    def cardexe(self):
        win32api.ShellExecute(0, 'open', 'CardClient-win32-x64\\CardClient.exe', '', '', 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainwindow()
    sys.exit(app.exec_())
