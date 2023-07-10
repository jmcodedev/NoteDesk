# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegistereNlRUx.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"\n"
"border-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Raleway Black\";\n"
"font-size: 28pt;")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 470))
        self.frame_2.setStyleSheet(u"QLabel {\n"
"	font: 63 12pt \"Raleway SemiBold\";\n"
"	color: rgb(0, 0, 0);\n"
"	margin-right:  15px;\n"
"}\n"
"QPushButton{	\n"
"	font: 63 12pt \"Raleway SemiBold\";\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: white;\n"
"	border-radius: 15px;\n"
"	width: 60px;\n"
"	height: 30px;\n"
"	font-size: 12px;\n"
"	text-align: center;\n"
"	line-height: 20px;\n"
"	text-decoration: none;\n"
"	display: inline-block;\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(80, 160, 240);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border: 2px solid #8707ff;\n"
"	border-radius: 10px;\n"
"	padding: 10px 25px;\n"
"	background: transparent;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.labelUsername = QLabel(self.frame_3)
        self.labelUsername.setObjectName(u"labelUsername")
        font = QFont()
        font.setFamily(u"Raleway SemiBold")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.labelUsername.setFont(font)
        self.labelUsername.setStyleSheet(u"")
        self.labelUsername.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.labelUsername)

        self.registerUsername = QLineEdit(self.frame_3)
        self.registerUsername.setObjectName(u"registerUsername")
        self.registerUsername.setMaximumSize(QSize(250, 50))
        self.registerUsername.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.registerUsername)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.labelUsername_2 = QLabel(self.frame_4)
        self.labelUsername_2.setObjectName(u"labelUsername_2")
        self.labelUsername_2.setFont(font)
        self.labelUsername_2.setStyleSheet(u"")
        self.labelUsername_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.labelUsername_2)

        self.registerPassword = QLineEdit(self.frame_4)
        self.registerPassword.setObjectName(u"registerPassword")
        self.registerPassword.setMaximumSize(QSize(250, 50))
        self.registerPassword.setStyleSheet(u"")
        self.registerPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.registerPassword)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 40)
        self.backButton = QPushButton(self.frame_6)
        self.backButton.setObjectName(u"backButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy2)
        self.backButton.setMaximumSize(QSize(50, 50))
        self.backButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.backButton.setStyleSheet(u"background-color: transparent;\n"
"padding-left: 20px;\n"
"")
        icon = QIcon()
        icon.addFile(u"icon pack/ATRAS.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.backButton)

        self.signupbutton = QPushButton(self.frame_6)
        self.signupbutton.setObjectName(u"signupbutton")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.signupbutton.sizePolicy().hasHeightForWidth())
        self.signupbutton.setSizePolicy(sizePolicy3)
        self.signupbutton.setMaximumSize(QSize(80, 50))
        self.signupbutton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signupbutton.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.signupbutton)


        self.verticalLayout.addWidget(self.frame_6)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.labelUsername.setText(QCoreApplication.translate("MainWindow", u"Nombre usuario", None))
        self.registerUsername.setText("")
        self.labelUsername_2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.backButton.setText("")
        self.signupbutton.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
    # retranslateUi

