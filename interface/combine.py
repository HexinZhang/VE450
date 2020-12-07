# coding: utf-8

# In[13]:
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
import option_wideget
from option_wideget import ChildButtonsetted,textwidget
from play_button import Child_Playbutton
from media_play import child_mediaplay
from media_play2 import child_chartplay
from image_with_mouse_control import ImageWithMouseControl
from media_play_three import child_mediaplay_three
# In[14]:


import sys
import urllib.request
import PyQt5
from PyQt5 import QtCore,QtGui,QtWidgets
import qtawesome
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl,QSize
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


# In[15]:


class Childbutton(QWidget):
    buttonevent_signal=pyqtSignal(int)
    def __init__(self, parent=None):
        super(Childbutton, self).__init__(parent)
        self.setGeometry(0,180, 300,50) 
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.BypassWindowManagerHint | Qt.Tool | Qt.WindowStaysOnTopHint)

        self.setWindowFlags( Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.main_layout = QVBoxLayout()
        self.top_widget = QWidget()
        self.setLayout(self.main_layout)
        self.top_widget.setObjectName("ChildOneWin_wdt")
        self.main_layout.addWidget(self.top_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        top_widget_layout = QVBoxLayout()
        self.top_widget.setLayout(top_widget_layout)

        self.test_btn = QPushButton('         ')
        self.test_btn.setStyleSheet(''' 
        
            QPushButton {text-align : center;  
            background-color :rgba(0,0,0,0); 
            border-color: rgba(0,0,0,0); 
           border-style: outset; font: Bold 30pt "Pristina"; color: rgb(157,157,157);}                
                     
                     ''')
        #self.test_btn.setFixedSize(300,5)
        self.test_btn.setFlat(True)
        top_widget_layout.addWidget(self.test_btn)
        self.test_btn.clicked.connect(self.buttonevent)
    def buttonevent(self):
        self.buttonevent_signal.emit(1)





class MainUi(QtWidgets.QMainWindow):
    main_widget_option_signal = pyqtSignal(int)
    main_widget_play_button_signal= pyqtSignal(int)
    main_widget_new_signal=pyqtSignal(int)
    main_widget_chart_play_signal=pyqtSignal(int)
    main_widget_chart_play_signal2=pyqtSignal(int)
    def __init__(self,parent=None):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.Option=0
        #gui.main_widget_signal.connect(option_func)
        self.setFixedSize(1500,800)
        
        self.setWindowIcon(QIcon('logo.png'))
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
        self.setWindowTitle('Group14 EV Charging Coordination Simulation Platform')
        wid2=QWidget()
        self.label=QLabel(wid2)    
        self.gif = QMovie('/Users/admin/Desktop/college/senior/VE450/better2.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        self.main_layout.addWidget(wid2)
        #self. child5_img=ImageWithMouseControl(self)
        #self.main_layout.addChildWidget(self.child5_img)
        #self.child6_button=Childbutton(self)
        
        #self.child6_button.hide()
        self.child2_play =Child_Playbutton(self) # 开始播放视频按钮
        self.main_layout.addChildWidget(self.child2_play)
        self.child1_options = ChildButtonsetted(self) # 灰色options列表在左上
        #self.main_layout.addChildWidget(self.child6_button)
        self.child1_options.hide()
        self.child3_mediaplay= child_mediaplay(self)
        self.child3_mediaplay.hide()
        self.main_layout.addChildWidget(self.child3_mediaplay)
        self.child4_mediaplay= child_chartplay(self)
        self.child4_mediaplay.hide()
        self.child5_mediaplay= child_mediaplay(self)
        self.child5_mediaplay.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/final_park.mp4")))
        
        self.child5_mediaplay.hide()
        self.child7_mediaplay= child_chartplay(self)
        
        self.child7_mediaplay.hide()
        
        self.child7_mediaplay.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/bar.mp4"))) 
        
        self.child8_mediaplay= child_chartplay(self)
        
        self.child8_mediaplay.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/guage.mp4")))
        self.child8_mediaplay.hide()
        self.child9_text=textwidget(self)
        self.child9_text.hide()
        


        self.main_layout.addChildWidget(self.child4_mediaplay)
        self.main_layout.addChildWidget(self.child5_mediaplay)
        self.main_layout.addChildWidget(self.child7_mediaplay)
        self.main_layout.addChildWidget(self.child8_mediaplay)
        self.main_layout.addChildWidget(self.child4_mediaplay)
        self.main_layout.addChildWidget(self.child1_options)
        self.main_layout.addChildWidget(self.child9_text)
        

        self.chart1Action= QAction('line',self)
        self.chart1Action.triggered.connect(lambda:self.mediaplaychange(1))
        self.nochartAction= QAction('no charts',self)
        self.nochartAction.triggered.connect(lambda:self.mediaplaychange(0))
        self.nochartAction.setShortcut('Esc')
        self.chart2Action= QAction('bar',self)
        self.chart2Action.triggered.connect(lambda:self.mediaplaychange(2))
        self.chart3Action= QAction('guage',self)
        self.chart3Action.triggered.connect(lambda:self.mediaplaychange(3))
        # Create exit action
        exitAction = QAction( '&Are you sure?', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.exitCall)
        
        self.scene1 = QAction('Overview', self,checkable=True)
        self.scene1.setChecked(True)
        self.scene1.triggered.connect(lambda:self.selectMenu(0))
        
        self.scene2 = QAction('Park1', self,checkable=True)
        self.scene2.setChecked(False)
        self.scene2.triggered.connect(lambda:self.selectMenu(1))

         # Create menu bar and add action
        self.menuBar = self.menuBar()
        self.fileMenu = self.menuBar.addMenu('&Select')
        self.fileMenu4=self.menuBar.addMenu('&charts')
        self.fileMenu2 = self.menuBar.addMenu('&Exit')
        self.fileMenu.addAction(self.scene1)
        self.fileMenu.addAction(self.scene2)
        self.fileMenu2.addAction(exitAction)
        self.fileMenu4.addAction(self.nochartAction)
        self.fileMenu4.addAction(self.chart1Action)
        self.fileMenu4.addAction(self.chart2Action)
        self.fileMenu4.addAction(self.chart3Action)
        
    def exitCall(self):
        sys.exit(app.exec_())
    def selectMenu(self, x):
       
        ## !!! Qction 自己会取消这个勾
        if x==0:
            self.scene1.setChecked(True)
            self.scene2.setChecked(False)
            self.Option=0
        if x==1:
            self.scene1.setChecked(False)
            self.scene2.setChecked(True)
            self.Option=1
        self.send_main_widget_option_signal()
    
    def send_main_widget_new_signal(self):
        self.main_widget_new_signal.emit(0)
    def send_main_widget_option_signal(self):
        self.main_widget_option_signal.emit(self.Option)
    def getOption(self):
        return self.Option
    def optionreset(self):
        self.Option=0
        self.main_widget_option_signal.emit(self.Option)
    def mediaplaychange(self,option):
        if self.Option ==0:
            self.main_widget_chart_play_signal.emit(option)
        else:
            self.main_widget_chart_play_signal2.emit(option)
def chart_pop(real_chart):
    
    gui.child3_mediaplay.hide()
    gui.child5_mediaplay.hide()

    real_chart.show()
    #self.main_widget_signal.emit(Option)
    animation4 = QPropertyAnimation(real_chart)
    animation4.setTargetObject(real_chart)
    #animation4.setPropertyName(b"pos")
    animation4.setPropertyName(b"geometry")
    x_start = -30
    y_start = -real_chart.height()
    point_start = QPoint(x_start, y_start)
    #animation4.setStartValue(point_start)
    #animation4.setStartValue(QtCore.QSize(400,300))
    animation4.setStartValue(QtCore.QRect(0,0,0,0))
    x_end = -30
    y_end = 0
    point_end = QPoint(x_end,y_end)
    #animation4.setEndValue(point_end)
    #animation4.setEndValue(QtCore.QSize(1600,800))
    animation4.setEndValue(QtCore.QRect(0,0,1500,800))
    animation4.setDuration(500)
    animation4.start(QAbstractAnimation.DeleteWhenStopped)
    
    animation4.setEasingCurve(QEasingCurve.InOutQuad) 
     #OutBounce 弹跳， InOutQuad 直接滑行
    real_chart.raise_()
    real_chart.raise_()
    real_chart.raise_()
def chart_hide():
    gui.child4_mediaplay.show()
    #self.main_widget_signal.emit(Option)
    animation4 = QPropertyAnimation(gui.child4_mediaplay)
    animation4.setTargetObject(gui.child4_mediaplay)
    #animation4.setPropertyName(b"pos")
    animation4.setPropertyName(b"geometry")
    animation4.setStartValue(QtCore.QRect(0,0,1500,800))
    #animation4.setStartValue(point_start)
    #animation4.setStartValue(QtCore.QSize(400,300))
    #animation4.setEndValue(point_end)
    #animation4.setEndValue(QtCore.QSize(1600,800))
    animation4.setEndValue(QtCore.QRect(0,0,0,0))
    animation4.setDuration(500)
    animation4.start(QAbstractAnimation.DeleteWhenStopped)
    animation4.setEasingCurve(QEasingCurve.InOutQuad)  #OutBounce 弹跳， InOutQuad 直接滑行
    gui.child4_mediaplay.hide()
    gui.child7_mediaplay.hide()
    gui.child8_mediaplay.hide()
def chart_widget_change_options2(Option):
    if Option==0:
        gui.child5_mediaplay.show()
        chart_hide()
    elif Option==1:
        chart_pop(gui.child4_mediaplay)
        gui.child7_mediaplay.hide()
        gui.child8_mediaplay.hide()
    elif Option==2:
        chart_pop(gui.child7_mediaplay)
        gui.child4_mediaplay.hide()
        gui.child8_mediaplay.hide()
    else:
        chart_pop(gui.child8_mediaplay)
        gui.child7_mediaplay.hide()
        gui.child4_mediaplay.hide()
def chart_widget_change_options(Option):
    if Option==0:
        gui.child3_mediaplay.show()
        chart_hide()
    elif Option==1:
        chart_pop(gui.child4_mediaplay)
        gui.child7_mediaplay.hide()
        gui.child8_mediaplay.hide()
    elif Option==2:
        chart_pop(gui.child7_mediaplay)
        gui.child4_mediaplay.hide()
        gui.child8_mediaplay.hide()
    else:
        chart_pop(gui.child8_mediaplay)
        gui.child7_mediaplay.hide()
        gui.child4_mediaplay.hide()
def child1_pop_options():
    
    gui.child2_play.hide()
    gui.child1_options.show()
    animation = QPropertyAnimation(gui.child1_options)
    animation.setTargetObject(gui.child1_options)
    animation.setPropertyName(b"pos")
    x_start = 1
    y_start = -gui.child1_options.height()
    point_start = QPoint(x_start, y_start)
    animation.setStartValue(point_start)
    x_end = 1
    y_end = 10
    point_end = QPoint(x_end,y_end)
    animation.setEndValue(point_end)
    animation.setDuration(1000)
    animation.start(QAbstractAnimation.DeleteWhenStopped)
    animation.setEasingCurve(QEasingCurve.OutBounce) 
    #gui.child6_button.show()
    gui.child9_text.show()
    animation = QPropertyAnimation(gui.child9_text)
    animation.setTargetObject(gui.child9_text)
    animation.setPropertyName(b"pos")
    x_start = 1
    y_start = -gui.child9_text.height()
    point_start = QPoint(x_start, y_start)
    animation.setStartValue(point_start)
    x_end = -8
    y_end = 640
    point_end = QPoint(x_end,y_end)
    animation.setEndValue(point_end)
    animation.setDuration(1000)
    animation.start(QAbstractAnimation.DeleteWhenStopped)
    animation.setEasingCurve(QEasingCurve.OutBounce) 
    #gui.child6_button.show()
def meida_pop_options(Option): 
    ## decide which media to pop 
    if Option == 0:
        gui.child5_mediaplay.hide()
        real_media_pop_options(gui.child3_mediaplay)
        
    if Option ==1:
        gui.child3_mediaplay.hide()
        real_media_pop_options(gui.child5_mediaplay)
def real_media_pop_options(real_media):     
        #pop the real media
        
        real_media.show()
        #self.main_widget_signal.emit(Option)
        animation = QPropertyAnimation(real_media)
        animation.setTargetObject(real_media)
        animation.setPropertyName(b"pos")
        x_start = 0
        y_start = real_media.height()
        point_start = QPoint(x_start, y_start)
        animation.setStartValue(point_start)
        x_end = 300
        y_end = -20
        point_end = QPoint(x_end,y_end)
        animation.setEndValue(point_end)
        animation.setDuration(1000)
        animation.start(QAbstractAnimation.DeleteWhenStopped)
        animation.setEasingCurve(QEasingCurve.InOutQuad)  #OutBounce 弹跳， InOutQuad 直接滑行
    #def optionmessage():
        
    #def optionmessage():

def meida_change_options(Option):
    
    if Option == 0  :
        gui.child3_mediaplay.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/final_overview.mp4")))
        gui.child3_mediaplay.playButton.setEnabled(True)    
    if Option == 1  :
        gui.child3_mediaplay.mediaPlayer.setMedia(
                    QMediaContent(QUrl.fromLocalFile("/Users/admin/Desktop/college/senior/VE450/parking_demo.avi")))
        gui.child3_mediaplay.playButton.setEnabled(True)    
def play_button_show(int):
    child2_play.show()
def mediaplay():
        
        if gui.child3_mediaplay.mediaPlayer.state() == QMediaPlayer.PlayingState:
            gui.child3_mediaplay.mediaPlayer.pause()
            gui.child4_mediaplay.mediaPlayer.pause()
            gui.child5_mediaplay.mediaPlayer.pause()
            #gui.child7_mediaplay.mediaPlayer.pause()
            #gui.child8_mediaplay.mediaPlayer.pause()
        else:
            gui.child3_mediaplay.mediaPlayer.play()
            gui.child4_mediaplay.mediaPlayer.play()
            gui.child5_mediaplay.mediaPlayer.play()
            #gui.child7_mediaplay.mediaPlayer.play()
            #gui.child8_mediaplay.mediaPlayer.play()
def printtext():
    gui.child9_text.printtext()        
        
        
 
# In[16]:


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    gui = MainUi()
    gui.show()
    
    gui.main_widget_option_signal.connect(meida_pop_options)
    gui.main_widget_play_button_signal.connect(play_button_show)
    gui.main_widget_chart_play_signal.connect(chart_widget_change_options)
    gui.main_widget_chart_play_signal2.connect(chart_widget_change_options2)

    gui.child2_play.play_signal.connect(lambda: meida_pop_options(0))
    gui.child2_play.play_signal.connect(child1_pop_options)
    gui.child2_play.play_signal.connect(mediaplay)
    gui.child2_play.play_signal.connect(printtext)
    #gui.child3_mediaplay.child_mediaplay_signal.connect(mediaplay)
    #gui.child4_mediaplay.child_chartplay_signal.connect(mediaplay)
    #gui.child5_mediaplay.child_mediaplay_signal.connect(mediaplay)
    #gui.child6_button.buttonevent_signal.connect(chart_pop)
    #gui.child7_mediaplay.child_chartplay_signal.connect(mediaplay)
    #gui.child8_mediaplay.child_chartplay_signal.connect(mediaplay)
 
    
    


    sys.exit(app.exec_())
