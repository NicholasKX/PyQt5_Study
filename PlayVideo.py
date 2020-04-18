# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playvideo.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 391, 331))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 70, 391, 331))
        self.label_2.setObjectName("label_2")
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setGeometry(QtCore.QRect(490, 90, 93, 28))
        self.pushButton_start.setObjectName("pushButton")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(490, 150, 93, 28))
        self.pushButton_stop.setObjectName("pushButton_2")
        # MainWindow.setCentralWidget(self.centralwidget)
        #         # self.menubar = QtWidgets.QMenuBar(MainWindow)
        #         # self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 26))
        #         # self.menubar.setObjectName("menubar")
        #         # MainWindow.setMenuBar(self.menubar)
        #         # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #         # self.statusbar.setObjectName("statusbar")
        #         # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_start.setText(_translate("MainWindow", "start"))
        self.pushButton_stop.setText(_translate("MainWindow", "stop"))
