# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProxyChanger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(292, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setGeometry(QtCore.QRect(0, 0, 291, 221))
        self.Tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.Tabs.setElideMode(QtCore.Qt.ElideNone)
        self.Tabs.setDocumentMode(False)
        self.Tabs.setTabsClosable(False)
        self.Tabs.setMovable(False)
        self.Tabs.setObjectName("Tabs")
        self.autoProxy = QtWidgets.QWidget()
        self.autoProxy.setObjectName("autoProxy")
        self.lblIp = QtWidgets.QLabel(self.autoProxy)
        self.lblIp.setGeometry(QtCore.QRect(10, 30, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblIp.setFont(font)
        self.lblIp.setObjectName("lblIp")
        self.lblPort = QtWidgets.QLabel(self.autoProxy)
        self.lblPort.setGeometry(QtCore.QRect(10, 60, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblPort.setFont(font)
        self.lblPort.setObjectName("lblPort")
        self.lblApiSite = QtWidgets.QLabel(self.autoProxy)
        self.lblApiSite.setGeometry(QtCore.QRect(10, 10, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblApiSite.setFont(font)
        self.lblApiSite.setObjectName("lblApiSite")
        self.btnGit1 = QtWidgets.QPushButton(self.autoProxy)
        self.btnGit1.setGeometry(QtCore.QRect(10, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGit1.setFont(font)
        self.btnGit1.setObjectName("btnGit1")
        self.txtLink1 = QtWidgets.QLineEdit(self.autoProxy)
        self.txtLink1.setGeometry(QtCore.QRect(10, 120, 271, 23))
        self.txtLink1.setObjectName("txtLink1")
        self.line = QtWidgets.QFrame(self.autoProxy)
        self.line.setGeometry(QtCore.QRect(10, 80, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.autoProxy)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 59, 15))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Tabs.addTab(self.autoProxy, "")
        self.manualProxy = QtWidgets.QWidget()
        self.manualProxy.setObjectName("manualProxy")
        self.label_6 = QtWidgets.QLabel(self.manualProxy)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 59, 15))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_2 = QtWidgets.QFrame(self.manualProxy)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btnGit2 = QtWidgets.QPushButton(self.manualProxy)
        self.btnGit2.setGeometry(QtCore.QRect(10, 150, 271, 31))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnGit2.setFont(font)
        self.btnGit2.setObjectName("btnGit2")
        self.label_7 = QtWidgets.QLabel(self.manualProxy)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtLink2 = QtWidgets.QLineEdit(self.manualProxy)
        self.txtLink2.setGeometry(QtCore.QRect(10, 120, 271, 23))
        self.txtLink2.setObjectName("txtLink2")
        self.label_8 = QtWidgets.QLabel(self.manualProxy)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtIp = QtWidgets.QLineEdit(self.manualProxy)
        self.txtIp.setGeometry(QtCore.QRect(80, 10, 201, 23))
        self.txtIp.setObjectName("txtIp")
        self.txtPort = QtWidgets.QLineEdit(self.manualProxy)
        self.txtPort.setGeometry(QtCore.QRect(80, 50, 201, 23))
        self.txtPort.setObjectName("txtPort")
        self.Tabs.addTab(self.manualProxy, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Tabs.setCurrentIndex(0)
        self.btnGit1.clicked.connect(MainWindow.siteyeGit_A)
        self.txtLink1.textChanged['QString'].connect(MainWindow.getLink1)
        self.txtIp.textChanged['QString'].connect(MainWindow.getIp)
        self.txtPort.textChanged['QString'].connect(MainWindow.getPort)
        self.txtLink2.textChanged['QString'].connect(MainWindow.getLink2)
        self.btnGit2.clicked.connect(MainWindow.siteyeGit_M)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Proxy Changer"))
        self.lblIp.setText(_translate("MainWindow", "IP : "))
        self.lblPort.setText(_translate("MainWindow", "PORT : "))
        self.lblApiSite.setText(_translate("MainWindow", "API SITE : "))
        self.btnGit1.setText(_translate("MainWindow", "SİTEYE GİT"))
        self.txtLink1.setText(_translate("MainWindow", "http://lemniskatarge.com"))
        self.label_4.setText(_translate("MainWindow", "LİNK"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.autoProxy), _translate("MainWindow", "Auto"))
        self.label_6.setText(_translate("MainWindow", "LİNK"))
        self.btnGit2.setText(_translate("MainWindow", "SİTEYE GİT"))
        self.label_7.setText(_translate("MainWindow", "PORT : "))
        self.txtLink2.setText(_translate("MainWindow", "http://lemniskatarge.com"))
        self.label_8.setText(_translate("MainWindow", "IP : "))
        self.Tabs.setTabText(self.Tabs.indexOf(self.manualProxy), _translate("MainWindow", "Manul"))
