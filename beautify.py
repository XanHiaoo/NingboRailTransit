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
                     background: rgb(255,255,255,180);
                     font: bold;
                     border-color: gray;
                     border-width: 2px;
                     border-radius: 10px;
                     padding: 6px;
                     height : 14px;
                     border-style: outset;
                     font : 15px;}
                     QPushButton:hover{
                     font: bold;
                     border: 1px solid Gray;
                     background:rgb(202,225,255,80);
                    }
                    QPushButton:pressed{
                    font: bold;
                    border: 2px solid DarkGray;
                    background:rgb(202,225,255, 100);
                    }

'''
# font = QtGui.QFont()
# font.setFamily('宋体')
labelstyle1='background:rgb(202,225,255,80);font: 25px;font-family:KaiTi'
labelstyle2='QLabel{color:rgb(28,28,28,255);font-size:40px;font-weight:normal;font-family:Microsoft Yahei;}'
labelstyle3='background:rgb(255,255,255,10);font: 25px;font-family:KaiTi'


QComboBoxstyle1='''
                QComboBox {border:none;background:rgb(202,225,255,80);color:#000000;
                padding-left:30px;font-size:15px "SimHei";}
                QComboBox QAbstractItemView { padding-left:30px;} 
                QComboBox QAbstractItemView:item { min-height: 100px; }
                QComboBox::drop-down {border:30px ;width: 20px;}
                '''




