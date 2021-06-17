
# -*- coding: utf-8 -*-

"""
PyQt5 tutorial 

In this example, we determine the event sender
object.

author: py40.com
last edited: 2017年3月
"""
from utils import *
import sys
import pandas as pd
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication,QPushButton,QVBoxLayout,QWidget,QDialog)
from PyQt5.QtGui import QIcon


class childwindownavi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/D:\\Users\\16030\\Desktop')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
                dd=pd.read_csv(fname[0],header=None,encoding="gbk")
                updateline(dd)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = childwindownavi()
    ex.show()
    sys.exit(app.exec_())