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

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWebChannel
import os 
#from PyQt5 import QtWebEngineWidgets

def webengine_hack():
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication.instance()
    if app is not None:
        import sip
        app.quit()
        sip.delete(app)
    import sys
    from PyQt5 import QtCore, QtWebEngineWidgets
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.qApp = QtWidgets.QApplication(sys.argv)
    return app

try:
    # just for testing
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication([''])
    from PyQt5 import QtWebEngineWidgets
    
except ImportError as exception:
    print('\nRetrying webengine import...')
    app = webengine_hack()
    from PyQt5 import QtWebEngineWidgets
    

class Ui_A7S_window(object):
  
    def setupUi(self, A7S_window):
        
        #self.setWindowTitle('CRO Road')
        
        A7S_window.setObjectName("Dialog")
        A7S_window.resize(1200, 1000)
        A7S_window.setMinimumSize(QtCore.QSize(552, 0))

        
        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)


        #label = self.label = QtWidgets.QLabel()
        
        #sp = QtWidgets.QSizePolicy()
        #sp.setVerticalStretch(0)
        
        #label.setSizePolicy(sp)
        #vbox.addWidget(label)
        
        view = self.view = QtWebEngineWidgets.QWebEngineView()
        
        channel = self.channel = QtWebChannel.QWebChannel()

        channel.registerObject("MainWindow", self)
        view.page().setWebChannel(channel)

        file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "data//html//A7.S.L0.R0.html",
        )
        
        self.view.setUrl(QtCore.QUrl.fromLocalFile(file))
        
        vbox.addWidget(view)
        

        
        self.centralwidget = QtWidgets.QWidget(A7S_window)
        self.centralwidget.setObjectName("centralwidget")
        #self.centralwidget.setCurrentIndex(2)

      
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 50, 30))
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

