# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import psutil

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 411)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 10, 221, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.OnClick)
        self.cpuusage = QtWidgets.QLabel(self.centralwidget)
        self.cpuusage.setGeometry(QtCore.QRect(10, 90, 401, 261))
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.cpuusage.setFont(font)
        self.cpuusage.setAlignment(QtCore.Qt.AlignCenter)
        self.cpuusage.setObjectName("cpuusage")
        self.cpuguide = QtWidgets.QLabel(self.centralwidget)
        self.cpuguide.setGeometry(QtCore.QRect(10, 60, 401, 18))
        self.cpuguide.setAlignment(QtCore.Qt.AlignCenter)
        self.cpuguide.setObjectName("cpuguide")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 423, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "A tiny little app"))
        self.pushButton.setText(_translate("MainWindow", "Hit this button!"))
        self.cpuguide.setText(_translate("MainWindow", "Your current CPU usage is:"))

    def OnClick(self):
        c = str(psutil.cpu_percent())
        self.cpuusage.setText(c)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
