# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:52:45 2020

@author: ll_stsekeid
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OtherWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from qtdesigner import Ui_MainWindow


class Ui_A7S_window(object):
  
    def setupUi(self, A7S_window):
        
        A7S_window.setObjectName("Dialog")
        A7S_window.resize(1200, 650)
        A7S_window.setMinimumSize(QtCore.QSize(552, 0))
        
        self.centralwidget = QtWidgets.QWidget(A7S_window)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setCurrentIndex(2)

      
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(110, 140, 141, 51))
        self.back_button.setObjectName("back")
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

        self.retranslateUi(A7S_window)
        QtCore.QMetaObject.connectSlotsByName(A7S_window)

    def retranslateUi(self, A7S_window):
        _translate = QtCore.QCoreApplication.translate
        A7S_window.setWindowTitle(_translate("A7S_window", "A7S_window"))
#        self.label.setText(_translate("OtherWindow", "A7 Süden 28 km"))
        self.back_button.setText(_translate("A7S_window", "zurück"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    A7S_window = QtWidgets.QMainWindow()
    ui = Ui_A7S_window()
    ui.setupUi(A7S_window)
    #A7S_window.show()
    sys.exit(app.exec_())

