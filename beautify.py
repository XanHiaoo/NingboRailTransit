# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 20:40
# @Author  : Han
# @File    : beautify.py
from PyQt5 import QtGui
qss ='''
                     QPushButton
                     {text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}
                     QPushButton:pressed
                     {text-align : center;
                     background-color : light gray;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}'''

buttonstyle1='''
                     QPushButton
                     {
                     text-align : center;
                     background-color : white;
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 14px;}
                     QPushButton:hover{
                     font: bold;
                     border: 1px solid Gray;
                     background:rgb(224, 238 ,224);
                    }
                    QPushButton:pressed{
                    font: bold;
                    border: 2px solid DarkGray;
                    background:rgb(0, 255, 0, 30);
                    }

'''
# font = QtGui.QFont()
# font.setFamily('宋体')





