1# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import Ui_OtherWindow




class Ui_MainWindow(object):
    
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        MainWindow.close()
        self.window.show()
            
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setCurrentIndex(1) #        
        
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(200, 210, 231, 61))
        self.button1.setObjectName("button1")
        self.button1.clicked.connect(self.openWindow)
        
        
        self.hsk = QtWidgets.QLabel(self.centralwidget)
        self.hsk.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.hsk.setText("")
        self.hsk.setPixmap(QtGui.QPixmap("img/hochschulekempten.jpg"))
        self.hsk.setScaledContents(True)
        self.hsk.setObjectName("hsk")
        self.adrive = QtWidgets.QLabel(self.centralwidget)
        self.adrive.setGeometry(QtCore.QRect(10, 60, 101, 31))
        self.adrive.setText("")
        self.adrive.setPixmap(QtGui.QPixmap("img/adrive.jpg"))
        self.adrive.setScaledContents(True)
        self.adrive.setObjectName("adrive")
        
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "First Button!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())