#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/18 
# @Author : XIAO
# @File : RunUi.py

import sys
import untitled

from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    ui=untitled.Ui_MainWindow()
    ui.setupUi(mainWindow)
    # ui.retranslateUi(mainWindow)
    # ui.initUI()
    mainWindow.show()
    sys.exit(app.exec_())

