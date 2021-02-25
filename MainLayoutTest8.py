# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Layouttest4.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 809)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setMinimumSize(QtCore.QSize(640, 360))
        self.webView.setUrl(QtCore.QUrl("https://www.tourtexas.com/assets/img/maps/san-antonio.jpg"))
        self.webView.setZoomFactor(2.0)
        self.webView.setObjectName("webView")
        self.verticalLayout_5.addWidget(self.webView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton, 0, QtCore.Qt.AlignTop)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignTop)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3, 0, QtCore.Qt.AlignTop)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4, 0, QtCore.Qt.AlignTop)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.octant_1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_1.sizePolicy().hasHeightForWidth())
        self.octant_1.setSizePolicy(sizePolicy)
        self.octant_1.setObjectName("octant_1")
        self.horizontalLayout_7.addWidget(self.octant_1)
        self.octant_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_2.sizePolicy().hasHeightForWidth())
        self.octant_2.setSizePolicy(sizePolicy)
        self.octant_2.setObjectName("octant_2")
        self.horizontalLayout_7.addWidget(self.octant_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.octant_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_3.sizePolicy().hasHeightForWidth())
        self.octant_3.setSizePolicy(sizePolicy)
        self.octant_3.setObjectName("octant_3")
        self.horizontalLayout_8.addWidget(self.octant_3)
        self.octant_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_4.sizePolicy().hasHeightForWidth())
        self.octant_4.setSizePolicy(sizePolicy)
        self.octant_4.setObjectName("octant_4")
        self.horizontalLayout_8.addWidget(self.octant_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.octant_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_5.sizePolicy().hasHeightForWidth())
        self.octant_5.setSizePolicy(sizePolicy)
        self.octant_5.setObjectName("octant_5")
        self.verticalLayout_4.addWidget(self.octant_5)
        self.octant_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_6.sizePolicy().hasHeightForWidth())
        self.octant_6.setSizePolicy(sizePolicy)
        self.octant_6.setObjectName("octant_6")
        self.verticalLayout_4.addWidget(self.octant_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.octant_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_7.sizePolicy().hasHeightForWidth())
        self.octant_7.setSizePolicy(sizePolicy)
        self.octant_7.setObjectName("octant_7")
        self.verticalLayout_3.addWidget(self.octant_7)
        self.octant_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.octant_8.sizePolicy().hasHeightForWidth())
        self.octant_8.setSizePolicy(sizePolicy)
        self.octant_8.setObjectName("octant_8")
        self.verticalLayout_3.addWidget(self.octant_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # Gives Black border around octants and MFD
        self.octant_1.setStyleSheet("border: 1px solid black;")
        self.octant_2.setStyleSheet("border: 1px solid black;")
        self.octant_3.setStyleSheet("border: 1px solid black;")
        self.octant_4.setStyleSheet("border: 1px solid black;")
        self.octant_5.setStyleSheet("border: 1px solid black;")
        self.octant_6.setStyleSheet("border: 1px solid black;")
        self.octant_7.setStyleSheet("border: 1px solid black;")
        self.octant_8.setStyleSheet("border: 1px solid black;")

        self.label.setStyleSheet("border: 1px solid black;")
        self.label_2.setStyleSheet("border: 1px solid black;")

        self.retranslateUi(MainWindow)

        # Layout 1
        self.pushButton.clicked.connect(self.octant_1.show)
        self.pushButton.clicked.connect(self.octant_2.hide)
        self.pushButton.clicked.connect(self.octant_3.hide)
        self.pushButton.clicked.connect(self.octant_4.hide)
        self.pushButton.clicked.connect(self.octant_5.hide)
        self.pushButton.clicked.connect(self.octant_6.hide)
        self.pushButton.clicked.connect(self.octant_7.hide)
        self.pushButton.clicked.connect(self.octant_8.hide)

        # Layout 2
        self.pushButton_2.clicked.connect(self.octant_1.show)
        self.pushButton_2.clicked.connect(self.octant_2.hide)
        self.pushButton_2.clicked.connect(self.octant_3.show)
        self.pushButton_2.clicked.connect(self.octant_4.hide)
        self.pushButton_2.clicked.connect(self.octant_5.show)
        self.pushButton_2.clicked.connect(self.octant_6.show)
        self.pushButton_2.clicked.connect(self.octant_7.hide)
        self.pushButton_2.clicked.connect(self.octant_8.hide)

        # Layout 3
        self.pushButton_3.clicked.connect(self.octant_1.show)
        self.pushButton_3.clicked.connect(self.octant_2.hide)
        self.pushButton_3.clicked.connect(self.octant_3.show)
        self.pushButton_3.clicked.connect(self.octant_4.hide)
        self.pushButton_3.clicked.connect(self.octant_5.hide)
        self.pushButton_3.clicked.connect(self.octant_6.show)
        self.pushButton_3.clicked.connect(self.octant_7.hide)
        self.pushButton_3.clicked.connect(self.octant_8.hide)
        # Layout 4
        self.pushButton_4.clicked.connect(self.octant_1.show)
        self.pushButton_4.clicked.connect(self.octant_2.hide)
        self.pushButton_4.clicked.connect(self.octant_3.hide)
        self.pushButton_4.clicked.connect(self.octant_4.hide)
        self.pushButton_3.clicked.connect(self.octant_2.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_4.clicked.connect(self.octant_5.show)
        self.pushButton_4.clicked.connect(self.octant_6.show)
        self.pushButton_4.clicked.connect(self.octant_7.hide)
        self.pushButton_4.clicked.connect(self.octant_8.hide)
        # Layout 5
        self.pushButton_5.clicked.connect(self.octant_1.show)
        self.pushButton_5.clicked.connect(self.octant_2.hide)
        self.pushButton_5.clicked.connect(self.octant_3.hide)
        self.pushButton_5.clicked.connect(self.octant_4.hide)
        self.pushButton_5.clicked.connect(self.octant_5.show)
        self.pushButton_5.clicked.connect(self.octant_6.hide)
        self.pushButton_5.clicked.connect(self.octant_7.hide)
        self.pushButton_5.clicked.connect(self.octant_8.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MFD1"))
        self.label_2.setText(_translate("MainWindow", "MFD2"))
        self.pushButton_6.setText(_translate("MainWindow", "Emergency Button"))
        self.pushButton_7.setText(_translate("MainWindow", "Testbutton2"))
        self.pushButton.setText(_translate("MainWindow", "Layout1"))
        self.pushButton_2.setText(_translate("MainWindow", "Layout2"))
        self.pushButton_3.setText(_translate("MainWindow", "Layout3"))
        self.pushButton_4.setText(_translate("MainWindow", "Layout4"))
        self.pushButton_5.setText(_translate("MainWindow", "Layout5"))
        self.octant_1.setText(_translate("MainWindow", "Octant 1"))
        self.octant_2.setText(_translate("MainWindow", "Octant 2"))
        self.octant_3.setText(_translate("MainWindow", "Octant 3"))
        self.octant_4.setText(_translate("MainWindow", "Octant 4"))
        self.octant_5.setText(_translate("MainWindow", "Octant 5"))
        self.octant_6.setText(_translate("MainWindow", "Octant 6"))
        self.octant_7.setText(_translate("MainWindow", "Octant 7"))
        self.octant_8.setText(_translate("MainWindow", "Octant 8"))
from PyQt5 import QtWebEngineWidgets
