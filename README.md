# NingboRailTransit
宁波轨道交通系统设计

### 环境：

```
## python
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
import pyodbc
import pandas as pd

## nopde.js
npm install electron

```



### 技术栈：

* SqlServer
* Python
* Pyqt5
* Html+Css+Js
* Node.js
* Electron 



###  说明：

* newui.py为y应用主界面。按钮“公交卡管理”关联启动了CardClient-win32-x64/文件夹下的CardClient.exe(已经打包好了运行所需环境)

* SqlServer的连接接口设置，位于两个位置。

  １．ｕｔｉｌｓ．ｐｙ

  ```
  函数名:sqllinkrail()
  功能:数据库连接
  
  
  函数名:sqllinkcard()
  功能:数据库连接
  
  ```

  ２．前段ｔｅｓｔ３文件夹下ｄｂ．ｊｓ

  

