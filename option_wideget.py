import sys
import string
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

class ChildButtonsetted(QWidget): # 覆盖图层
    child_widget_signal = pyqtSignal(int) #带一个参数（字典）的信号
    def __init__(self, parent=None):
        super(ChildButtonsetted, self).__init__(parent)
        
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(200)
        self.shadow.setColor(QColor(85, 123, 182))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow2 = QGraphicsDropShadowEffect()
        self.shadow2.setBlurRadius(5)
        self.shadow2.setXOffset(5)
        self.shadow2.setYOffset(5)
        self.setGraphicsEffect(self.shadow2)
        self.resize(340,640)
        
        self.wdt = QWidget()
        #self.wdt.setAttribute(Qt.WA_TranslucentBackground)
        self.wdt.setObjectName("tipWaitingWindow_back")
        self.wdt.setStyleSheet("#tipWaitingWindow_back{background:rgba(0,0,0,0.2)}")
        
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.wdt)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        #self.main_layout = QGridLayout(self)
        self.main_layout = QVBoxLayout(self)
        self.wdt.setLayout(self.main_layout)
        
        self.webEngineView = QWebEngineView()
        self.webEngineView.load(QUrl('file:///C://Users/admin/Desktop/college/senior/VE450/page_simple_layoutnew.html'))
        #self.webEngineView2.load(QUrl('file:///C://Users/admin/Desktop/college/senior/VE450/timeline_bar(1).html'))
        #self.webEngineView3.load(QUrl('file:///C://Users/admin/Desktop/college/senior/VE450/gauge.html'))
        #self.webEngineView4.load(QtCore.QUrl('timeline_bar(1).html'))
        #self.main_layout.addWidget(self.webEngineView,4,0,4,3)
        #self.main_layout.addWidget(self.webEngineView2,4,3,4,3)
        #self.main_layout.addWidget(self.webEngineView3,8,0,4,3)
        self.main_layout.addWidget(self.webEngineView)
        #self.main_layout.addWidget(self.webEngineView2)
        #self.main_layout.addWidget(self.webEngineView3)
        #self.main_layout.addWidget(self.webEngineView4,8,3,4,3)


    def slot_next_btn_func(self):
        self.child_widget_signal.emit(1)


class textwidget(QWidget):
    child_widget_signal = pyqtSignal(int) #带一个参数（字典）的信号
    def __init__(self, parent=None):
        super(textwidget, self).__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.resize(355,300)
        self.process = QTextEdit(self, readOnly=True)
        self.process.ensureCursorVisible()
        self.process.setLineWrapColumnOrWidth(500)
        self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.process.setStyleSheet('''background-color: rgba(0,0,0,0.2); color: rgb(250,250,250);
        font: Bold 10pt ;border: none;''')
        self.layout =QVBoxLayout(self)
        self.layout.addWidget(self.process)
        
        #self.show()
    def printtext(self):
        print('Running...')
        with open('/Users/admin/Desktop/college/senior/VE450/wfile.txt','r') as reader:
            line = reader.readline() #time
            line1 = reader.readline()
            line2 = line1 +reader.readline()
            while line:
                self.process.setPlainText(line2)
                loop = QEventLoop() 
                QTimer.singleShot(2000, loop.quit) #/ms
                loop.exec_()
                line = reader.readline() #time
                line1 = reader.readline()
                line2 = line1 + reader.readline()
