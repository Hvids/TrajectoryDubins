import os, math, sys
import matplotlib.pyplot as plt
import numpy as np
import ModelTrajectory as models
import DrawTrajectory
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip
from PyQt5.QtWidgets import QPushButton, QDesktopWidget, QHBoxLayout
from PyQt5.QtWidgets import  QVBoxLayout, QLabel, QLineEdit,QGridLayout
from PyQt5.QtGui import QIcon, QFont,QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QFileInfo,QCoreApplication


#Сохраняем рисунок



class Error(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print ("Error")
        box = QVBoxLayout()
        self.setLayout(box)
        self.setHelpPage()
        self.window()

    def setHelpPage(self):
        self.clearLayout(self.layout())
        bthOk = self.buttonOk()
        webview = QWebEngineView()
        webview.load(QUrl.fromLocalFile(QFileInfo('../templates/html/error.html').absoluteFilePath()))
        layout =  self.displayHelp(bthOk,webview)
        self.layout().addLayout(layout)

    def displayHelp(self,bth,text):
        vbox = QVBoxLayout()
        vbox.addWidget(text)
        vbox.addStretch(1)
        vbox.addWidget(bth)
        vbox.addSpacing(15)
        return vbox

    def buttonOk(self):
        bth = QPushButton('OK')
        bth.setToolTip('<b>Push</b> for continur work work' )
        bth.resize(bth.sizeHint())
        bth.clicked.connect(self.deleteLater)
        return bth

    def window(self):
        self.resize(300,300)
        self.center()
        self.setWindowTitle("Eror")
        self.setWindowIcon(QIcon("../templates/img/icon.png"))
        self.show()

    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clearLayout(self,layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

class Hepl(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        print ("Help")
        box = QVBoxLayout()
        self.setLayout(box)
        self.setHelpPage()
        self.window()

    def setHelpPage(self):
        self.clearLayout(self.layout())
        bthOk = self.buttonOk()
        webview = QWebEngineView()
        webview.load(QUrl.fromLocalFile(QFileInfo('../templates/html/help.html').absoluteFilePath()))
        layout =  self.displayHelp(bthOk,webview)
        self.layout().addLayout(layout)

    def displayHelp(self,bth,text):
        vbox = QVBoxLayout()
        vbox.addWidget(text)
        vbox.addStretch(1)
        vbox.addWidget(bth)
        vbox.addSpacing(15)
        return vbox

    def buttonOk(self):
        bth = QPushButton('OK')
        bth.setToolTip('<b>Push</b> for continur work work' )
        bth.resize(bth.sizeHint())
        bth.clicked.connect(self.deleteLater)
        return bth

    def window(self):
        self.resize(300,300)
        self.center()
        self.setWindowTitle("Help")
        self.setWindowIcon(QIcon("../templates/img/icon.png"))
        self.show()

    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clearLayout(self,layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

class Project(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        layout =  QVBoxLayout()
        self.setLayout(layout)
        self.setIndexPage()
        self.window()

    #ErorEnterData
    def errorEntetData(self,text1,text2):
        list1 = text1.split()
        list2 = text2.split()
        if (len(list1)!=3 or len(list2)!=3):
            return False
        list_number =[]
        for n in list1:
            try:
                f = float(n)
                list_number.append(f)
            except ValueError:
                return False
        list_number[2] = math.pi*list_number[2]/180
        self.PointStart = models.Position(list_number[0],list_number[1],list_number[2])
        list_number =[]
        for n in list2:
            try:
                f = float(n)
                list_number.append(f)
            except ValueError:
                return False
        list_number[2] = math.pi*list_number[2]/180
        self.PointFinish = models.Position(list_number[0],list_number[1],list_number[2])
        return True


    #setPage
    def setResultPage(self):
        self.clearLayout(self.layout())
        layout = self.ResultPage()
        self.layout().addLayout(layout)

    def setIndexPage(self):
        self.clearLayout(self.layout())
        layout = self.IndexPage()
        self.layout().addLayout(layout)

    def setEnterDataPage(self):
        self.clearLayout(self.layout())
        layout = self.EnterDataPage()
        self.layout().addLayout(layout)

    #Page
    def ResultPage(self):

        bthRestart = self.buttonRestart()
        bthExit = self.buttonExit()
        img =  QPixmap('../templates/img/trajectory.png')
        label = QLabel()
        label.setPixmap(img)
        layout = self.displayResult(bthRestart,bthExit,label)
        return layout

    def IndexPage(self):
        bthStart = self.buttonStart()
        bthExit = self.buttonExit()
        bthHelp = self.buttonHelp()
        layout = self.displayIndex(bthStart = bthStart,bthHelp = bthHelp,bthExit = bthExit)
        return layout

    def EnterDataPage(self):
        bthEnter = self.buttonEnter()
        bthExit = self.buttonExit()
        bthHelp = self.buttonHelp()
        title_start = QLabel('Start')
        title_finish = QLabel('Finish')
        self.startData = QLineEdit()
        self.finishData = QLineEdit()
        self.startData.resize(self.startData.sizeHint())
        self.finishData.resize(self.finishData.sizeHint())
        layout = self.dislpayEnterData(bthEnter,bthHelp,bthExit,title_start,title_finish)
        return layout

    #Display
    def displayResult(self,bth1,bth2,img):
        vbox = QVBoxLayout()
        hboxBth1 = QHBoxLayout()
        hboxBth2 = QHBoxLayout()

        vbox.addWidget(img)

        hboxBth1.addStretch(1)
        hboxBth1.addWidget(bth1)
        vbox.addLayout(hboxBth1)

        hboxBth2.addStretch(1)
        hboxBth2.addWidget(bth2)

        vbox.addStretch(1)
        vbox.addLayout(hboxBth2)
        return vbox

    def displayIndex(self,bthStart,bthHelp,bthExit):
        vbox = QVBoxLayout()

        hboxStart = QHBoxLayout()
        hboxStart.addStretch(1)
        hboxStart.addWidget(bthStart)

        hboxHelp = QHBoxLayout()
        hboxHelp.addStretch(1)
        hboxHelp.addWidget(bthHelp)

        hboxExit = QHBoxLayout()
        hboxExit.addStretch(1)
        hboxExit.addWidget(bthExit)

        vbox.addSpacing(10)
        vbox.addLayout(hboxStart)
        vbox.addSpacing(30)
        vbox.addLayout(hboxHelp)
        vbox.addStretch(1)
        vbox.addLayout(hboxExit)

        grid = QGridLayout()
        grid.addLayout(vbox,1,1)
        return grid

    def dislpayEnterData(self,bth1,bth2, bth3, title1,title2):
        hboxStart = QHBoxLayout()
        hboxStart.addWidget(title1)
        hboxStart.addWidget(self.startData)
        hboxFinish = QHBoxLayout()
        hboxFinish.addWidget(title2)
        hboxFinish.addWidget(self.finishData)
        hboxBth1 = QHBoxLayout()
        hboxBth1.addStretch(1)
        hboxBth1.addWidget(bth1)


        vboxBth2_3 = QVBoxLayout()
        vboxBth2_3.addWidget(bth2)
        vboxBth2_3.addStretch(1)
        vboxBth2_3.addWidget(bth3)

        vboxLayout1 = QVBoxLayout()
        vboxLayout1.addLayout(hboxStart)
        vboxLayout1.addLayout(hboxFinish)
        vboxLayout1.addLayout(hboxBth1)
        vboxLayout1.addStretch(1)

        hboxLayouy2 = QHBoxLayout()
        hboxLayouy2.addLayout(vboxLayout1)
        hboxLayouy2.addLayout(vboxBth2_3)
        return hboxLayouy2

    #Clicked
    def buttonClickedRestart(self):
        self.setEnterDataPage()

    def buttonClickedStart(self):
        self.setEnterDataPage()

    def buttonClickedHelp(self):
        self.help = Hepl()

    def buttonClickedEnter(self):
        self.start_coordinate = self.startData.text()
        self.finish_coordinate = self.finishData.text()
        if self.errorEntetData(self.start_coordinate,self.finish_coordinate):
            DrawTrajectory.drawTrajectory(self.PointStart,self.PointFinish)
            self.setResultPage()
        else:
            self.error= Error()

    #Button
    def buttonRestart(self):
        bth = QPushButton('Restart')
        bth.setToolTip('<b>Push</b> after enter data')
        bth.resize(bth.sizeHint())
        bth.clicked.connect(self.buttonClickedRestart)
        return bth

    def buttonEnter(self):
        bth = QPushButton('Enter')
        bth.setToolTip('<b>Push</b> after enter data')
        bth.resize(bth.sizeHint())
        bth.clicked.connect(self.buttonClickedEnter)
        return bth

    def buttonStart(self):
        bth = QPushButton('Start')
        bth.setToolTip('<b>Push</b> for start work' )
        bth.resize(bth.sizeHint())
        bth.clicked.connect(self.buttonClickedStart)
        return bth

    def buttonHelp(self):
        bth = QPushButton('Help')
        bth.setToolTip('<b>Push</b> for  help')
        bth.clicked.connect(self.buttonClickedHelp)
        bth.resize(bth.sizeHint())
        return bth

    def buttonExit(self):
        bth = QPushButton('Exit')
        bth.clicked.connect(QCoreApplication.instance().quit)
        bth.resize(bth.sizeHint())
        return bth

    #Setting
    def window(self):
        self.resize(600,600)
        self.center()
        self.setWindowTitle("Trajectory Dubins")
        self.setWindowIcon(QIcon("../templates/img/icon.png"))
        self.show()

    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def clearLayout(self,layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())







# Добавление на рисунок прямоугольной (по умолчанию) области
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dubins = Project()
    sys.exit(app.exec_())


#save(name='pic_1',fmt='png')
