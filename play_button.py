import sys

import PyQt5
from PyQt5 import QtCore,QtGui,QtWidgets
import qtawesome
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFrame
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QGuiApplication


import sys
import urllib.request
import PyQt5
from PyQt5 import QtCore,QtGui,QtWidgets
import qtawesome
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import * 
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFrame,QGraphicsDropShadowEffect
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFrame
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import urllib.request

class Child_Playbutton(QWidget): #用作optio 
    play_signal=pyqtSignal(int)
    def __init__(self, parent=None):
        super(Child_Playbutton, self).__init__(parent)
        self.resize(1400,600)
        self.Option=parent.getOption()
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(200)
        self.shadow.setColor(QColor(255,255,255))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.BypassWindowManagerHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.wdt = QWidget()
        #self.wdt.setObjectName("tipWaitingWindow_back")
        #self.wdt.setStyleSheet("#tipWaitingWindow_back{background:rgba(0,0,0,0.2)}")
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
        
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.wdt,8,6,16,5)
        self.layout.addWidget(self.left_widget,0,6,16,5)
        
        self.layout.setSpacing(100)
        main_layout = QGridLayout()

        self.wdt.setLayout(main_layout)
        # 在main_layout上添加widget就行
        
        self.Play_button = QPushButton('Play')
        self.Play_button.setFixedSize(120,70)
        self.Play_button.setStyleSheet(''' 
        
            QPushButton {text-align : center;  
            background-color :rgba(0,0,0,0); 
            border-color: rgba(0,0,0,0); border-width: 2px; border-radius: 10px; 
            height : 60px; border-style: outset; font: Bold 30pt "Pristina"; color: rgb(157,157,157);}
        QPushButton:hover{ font: Bold 30pt "Pristina"; 
        color: rgb(255,255,255);
            border-color: rgb(85, 123, 182);
            border-width: 2px;
            border-radius: 10px; padding: 0px;
                     height : 30px;
                     border-style: outset; background: rgba(0,0,0,0.2)}
         QPushButton:press{ font: Bold 30pt "Pristina"; color: rgb(255,255,255);
            border-color: rgb(85, 123, 182);border-width: 2px;
            border-radius: 10px; padding: 6px;
                     height : 14px;
                     border-style: outset; background: rgba(0,0,0,0.4)}            
                     
                     
                     ''')
        self.Play_button.setGraphicsEffect(self.shadow)
        main_layout.addWidget(self.Play_button,8,10,6,5)
        self.Play_button.clicked.connect(self.play)
    def play(self):
        self.play_signal.emit(1)
       #self.Menu_button.clicked.connect()
    def getOption(self):
        return self.Option