# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(283, 92)
        MainWindow.setMinimumSize(QtCore.QSize(283, 92))
        MainWindow.setMaximumSize(QtCore.QSize(283, 92))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblLength = QtWidgets.QLabel(self.centralwidget)
        self.lblLength.setGeometry(QtCore.QRect(14, 22, 113, 16))
        self.lblLength.setObjectName("lblLength")
        self.textLength = QtWidgets.QLineEdit(self.centralwidget)
        self.textLength.setGeometry(QtCore.QRect(136, 20, 39, 20))
        self.textLength.setAlignment(QtCore.Qt.AlignCenter)
        self.textLength.setObjectName("textLength")
        self.pushButtonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(190, 18, 75, 23))
        self.pushButtonGenerate.setObjectName("pushButtonGenerate")
        self.textGenerated = QtWidgets.QLineEdit(self.centralwidget)
        self.textGenerated.setGeometry(QtCore.QRect(16, 56, 249, 20))
        self.textGenerated.setText("")
        self.textGenerated.setAlignment(QtCore.Qt.AlignCenter)
        self.textGenerated.setObjectName("textGenerated")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password generator"))
        self.lblLength.setText(_translate("MainWindow", "Number of characters:"))
        self.textLength.setText(_translate("MainWindow", "8"))
        self.pushButtonGenerate.setText(_translate("MainWindow", "Generate!"))

