# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from qtdesigner import Ui_MainWindow


class Ui_OtherWindow(object):

#    def openWindow(self):
#        self.window = QtWidgets.QMainWindow()
#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self.window)
#        OtherWindow.hide()
#        self.window.show()    
    
    
    
    def setupUi(self, OtherWindow):
        
        OtherWindow.setObjectName("Dialog")
        OtherWindow.resize(1200, 650)
        OtherWindow.setMinimumSize(QtCore.QSize(552, 0))
        
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setCurrentIndex(2)
        
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(110, 140, 141, 51))
        self.btn_open.setObjectName("btn_open")
        #self.btn_open.clicked.connect(self.openWindow)
        
        
        #self.btn_open.clicked.connect(self.openWindow)
        
#        self.label = QtWidgets.QLabel(self.centralwidget)
#        self.label.setGeometry(QtCore.QRect(110, 30, 371, 41))
#        font = QtGui.QFont()
#        font.setPointSize(22)
#        self.label.setFont(font)
#        self.label.setObjectName("label")
        #OtherWindow.setCentralWidget(self.centralwidget)
        
        
        
#        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
#        self.statusbar.setObjectName("statusbar")
#        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "OtherWindow"))
#        self.label.setText(_translate("OtherWindow", "A7 Süden 28 km"))
        self.btn_open.setText(_translate("OtherWindow", "zurück"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())

