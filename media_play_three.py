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


class child_mediaplay_three(QWidget):
    child_mediaplay_signal=pyqtSignal(int)
    def __init__(self, parent=None):
        super(child_mediaplay_three, self).__init__(parent)
  
        
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.resize(340,640)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        # Create a widget for window contents
        self.wdt = QWidget()
        self.wdt.setObjectName("tipWaitingWindow_back")
        self.wdt.setStyleSheet("#tipWaitingWindow_back{background:rgba(0,0,0,0.2)}")
        
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(5,5,5,5)
        self.layout.addWidget(self.wdt)
        
        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        #layout.addLayout(controlLayout)
        #layout.addWidget(self.errorLabel)
        
        # Set widget to contain window contents
        self.wdt.setLayout(layout)
        
        self.mediaPlayersetmovie_func(parent.getOption())
        
        self.mediaPlayer.setVideoOutput(videoWidget)
        
        
    def mediaPlayersetmovie_func(self,Option): # add video into the playlist
            #playlist=QMediaPlaylist()
            #url1=QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/WeChat_20201101182322.mp4") # the filepath of the video
            #url2=Qurl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/941f737bbefa90786690692e2fa7b54d.mp4")
            #playlist.addMedia(QMediaContent(url))
            #playlist.addMedia(QMediaContent(ur2))
            #player.setPlaylist(playlist)
            
        self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/three.mp4"))) 
        
            
            
    