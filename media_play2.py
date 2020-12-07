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
import option_wideget
from option_wideget import ChildButtonsetted
from play_button import Child_Playbutton
# In[14]:


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

# In[14]:


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import urllib.request


class child_chartplay(QWidget):
    child_chartplay_signal=pyqtSignal(int)
    def __init__(self, parent=None):
        super(child_chartplay, self).__init__(parent)
  
        self.setWindowFlags( QtCore.Qt.WindowMinimizeButtonHint|Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        #self.effect = QGraphicsOpacityEffect()
        #self.effect= qr.setOpacity(0.9)
        #self.setGraphicsEffect(effect)

        
        self.resize(1500,800)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        # Create a widget for window contents
        self.wdt = QWidget()
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格
        #self.wdt.setAttribute(Qt.WA_TranslucentBackground)
        self.wdt.setObjectName("tipWaitingWindow_back")
        self.wdt.setStyleSheet("#tipWaitingWindow_back{background:rgba(0,0,0,0.2)}")
        
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(10,10,10,10)
        self.layout.addWidget(self.wdt,1,2,15,9)
        self.layout.addWidget(self.left_widget,0,0,16,2) # 左侧部件在第0行第0列，占8行3列
        #self.main_layout.addWidget(self.right_widget,0,2,16,8.5) # 左侧部件在第0行第0列，占8行3列
        self.top_layout=QVBoxLayout()
        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.signal_emit)
        
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Maximum)
        
        # Create layouts to place inside widget
        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0,0,0,0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)
        
        # Set widget to contain window contents
        self.wdt.setLayout(layout)
        
        self.mediaPlayersetmovie_func()
        
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)

        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
    def signal_emit(self):
        self.child_mediaplay_signal.emit(1)    
    def mediaPlayersetmovie_func(self): # add video into the playlist
            #playlist=QMediaPlaylist()
            #url1=QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/WeChat_20201101182322.mp4") # the filepath of the video
            #url2=Qurl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/941f737bbefa90786690692e2fa7b54d.mp4")
            #playlist.addMedia(QMediaContent(url))
            #playlist.addMedia(QMediaContent(ur2))
            #player.setPlaylist(playlist)
        self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/line_new.mp4"))) 
        self.playButton.setEnabled(True)
            
    
    def exitCall(self):
        sys.exit(app.exec_())

    def play(self):
        
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
            
        else:
            self.mediaPlayer.play()
        
    def mediaStateChanged(self, state):
        
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)
        
    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def on_combobox_func(self,text):
        self.current_text= text
        print(1)
