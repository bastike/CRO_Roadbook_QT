# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:04:21 2020

@author: ll_stsekeid
"""

from PyQt5 import QtWidgets

from qtdesigner import Ui_MainWindow
from OtherWindow import Ui_OtherWindow
from A7S_window import Ui_A7S_window

class Firstwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Firstwindow, self).__init__(parent)
        self.setupUi(self)
        #self.button1.clicked.connect(self.hide) #close MainWindow when opening another window 


class Secondwindow(QtWidgets.QDialog, Ui_OtherWindow):
    def __init__(self, parent=None):
        super(Secondwindow, self).__init__(parent)
        self.setupUi(self)
        self.btn_open.clicked.connect(self.hide)


class A7Swindow(QtWidgets.QDialog, Ui_A7S_window):
    def __init__(self, parent=None):
        super(A7Swindow, self).__init__(parent)
        self.setupUi(self)
        self.back_button.clicked.connect(self.hide)


class Manager:
    def __init__(self):
        self.first = Firstwindow()
        self.second = Secondwindow()
        self.A7S = A7Swindow()

        self.first.button1.clicked.connect(self.second.show)
        self.first.buttonA7S.clicked.connect(self.A7S.show)
        
        self.second.btn_open.clicked.connect(self.first.show)
        self.A7S.back_button.clicked.connect(self.first.show)
        
        self.first.show()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())