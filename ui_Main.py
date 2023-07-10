# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainykxnqF.ui'
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
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1114, 834)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setEnabled(True)
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setTabletTracking(False)
        self.frame_superior.setStyleSheet(u"QFrame{\n"
"	background-color: #B6CFF2;\n"
"	\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QFrame.NoFrame)
        self.frame_superior.setFrameShadow(QFrame.Plain)
        self.frame_superior.setLineWidth(1)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 4, 0)
        self.btnMenu = QPushButton(self.frame_superior)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setMaximumSize(QSize(20, 20))
        self.btnMenu.setFocusPolicy(Qt.StrongFocus)
        self.btnMenu.setStyleSheet(u"QPushButton{\n"
"border-radius: 12px;\n"
"height: 20px;\n"
"width: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"background-color: #d7f3ff;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../TFG/icon pack/MENU.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMenu.setIcon(icon)
        self.btnMenu.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btnMenu)

        self.horizontalSpacer = QSpacerItem(826, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnMinimizar = QPushButton(self.frame_superior)
        self.btnMinimizar.setObjectName(u"btnMinimizar")
        self.btnMinimizar.setMaximumSize(QSize(20, 20))
        self.btnMinimizar.setFocusPolicy(Qt.StrongFocus)
        self.btnMinimizar.setAcceptDrops(True)
        self.btnMinimizar.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"height: 30px;\n"
"width: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"background-color: #FAF186;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../TFG/icon pack/MINIMIZE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMinimizar.setIcon(icon1)
        self.btnMinimizar.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btnMinimizar)

        self.btnMaximizar = QPushButton(self.frame_superior)
        self.btnMaximizar.setObjectName(u"btnMaximizar")
        self.btnMaximizar.setMaximumSize(QSize(20, 20))
        self.btnMaximizar.setFocusPolicy(Qt.StrongFocus)
        self.btnMaximizar.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"height: 30px;\n"
"width: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"background-color: #C0FAAD;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../TFG/icon pack/MAXIMIZE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMaximizar.setIcon(icon2)
        self.btnMaximizar.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btnMaximizar)

        self.btnRestaurar = QPushButton(self.frame_superior)
        self.btnRestaurar.setObjectName(u"btnRestaurar")
        self.btnRestaurar.setMaximumSize(QSize(20, 20))
        self.btnRestaurar.setFocusPolicy(Qt.StrongFocus)
        self.btnRestaurar.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"height: 30px;\n"
"width: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"background-color: #C0FAAD;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../TFG/icon pack/RESTORE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRestaurar.setIcon(icon3)
        self.btnRestaurar.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btnRestaurar)

        self.btnCerrar = QPushButton(self.frame_superior)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setMaximumSize(QSize(20, 20))
        self.btnCerrar.setFocusPolicy(Qt.StrongFocus)
        self.btnCerrar.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"height: 30px;\n"
"width: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 0px;\n"
"background-color: #E0A09A;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../../TFG/icon pack/CLOSE WINDOW.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnCerrar.setIcon(icon4)
        self.btnCerrar.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btnCerrar)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_inferior)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(0, 0))
        self.frame_menu.setMaximumSize(QSize(0, 16777215))
        self.frame_menu.setStyleSheet(u"QFrame{\n"
"	background-color: #B6CFF2;\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding-left: 30px;\n"
"	padding-right: 30px;\n"
"	border-radius: 15px;	\n"
"	font: 63 12pt \"Raleway SemiBold\";\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: #CEDFF6;\n"
"	border-radius: 15px;\n"
"	\n"
"	font: 81 12pt \"Raleway ExtraBold\";\n"
"}")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 1)
        self.bt_inicio = QPushButton(self.frame_menu)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        self.bt_inicio.setMaximumSize(QSize(16777215, 40))
        icon5 = QIcon()
        icon5.addFile(u"../../TFG/icon pack/HOME.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon5)
        self.bt_inicio.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.bt_inicio)

        self.bt_Buscar = QPushButton(self.frame_menu)
        self.bt_Buscar.setObjectName(u"bt_Buscar")
        self.bt_Buscar.setMinimumSize(QSize(0, 40))
        self.bt_Buscar.setMaximumSize(QSize(16777215, 40))
        icon6 = QIcon()
        icon6.addFile(u"../../TFG/icon pack/SEARCH.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Buscar.setIcon(icon6)
        self.bt_Buscar.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.bt_Buscar)

        self.bt_Editar = QPushButton(self.frame_menu)
        self.bt_Editar.setObjectName(u"bt_Editar")
        self.bt_Editar.setMinimumSize(QSize(0, 40))
        self.bt_Editar.setMaximumSize(QSize(16777215, 40))
        icon7 = QIcon()
        icon7.addFile(u"../../TFG/icon pack/EDIT.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Editar.setIcon(icon7)
        self.bt_Editar.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.bt_Editar)

        self.bt_Borrado = QPushButton(self.frame_menu)
        self.bt_Borrado.setObjectName(u"bt_Borrado")
        self.bt_Borrado.setMinimumSize(QSize(0, 40))
        self.bt_Borrado.setMaximumSize(QSize(16777215, 40))
        icon8 = QIcon()
        icon8.addFile(u"../../TFG/icon pack/DELETE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Borrado.setIcon(icon8)
        self.bt_Borrado.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.bt_Borrado)

        self.bt_Ayuda = QPushButton(self.frame_menu)
        self.bt_Ayuda.setObjectName(u"bt_Ayuda")
        self.bt_Ayuda.setMinimumSize(QSize(0, 40))
        self.bt_Ayuda.setMaximumSize(QSize(16777215, 40))
        icon9 = QIcon()
        icon9.addFile(u"../../TFG/icon pack/INFO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Ayuda.setIcon(icon9)
        self.bt_Ayuda.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.bt_Ayuda)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.madeBy = QLabel(self.frame_menu)
        self.madeBy.setObjectName(u"madeBy")
        self.madeBy.setStyleSheet(u"font: 63 italic 9pt \"Raleway SemiBold\";")
        self.madeBy.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.madeBy)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_ventana = QFrame(self.frame_inferior)
        self.frame_ventana.setObjectName(u"frame_ventana")
        self.frame_ventana.setFrameShape(QFrame.StyledPanel)
        self.frame_ventana.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_ventana)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_ventana)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.p_Inicio = QWidget()
        self.p_Inicio.setObjectName(u"p_Inicio")
        self.verticalLayout_4 = QVBoxLayout(self.p_Inicio)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.p_Inicio)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"}\n"
"#n1, #n10, #n20, #n18 {\n"
"	background-color: rgb(251, 229, 147);\n"
"}\n"
"#n2, #n7, #n16, #n19 {\n"
"	background-color: rgb(206, 234, 171);\n"
"}\n"
"#n3, #n12, #n14, #n21 {\n"
"	background-color: rgb(254, 178, 135);\n"
"}\n"
"#n4, #n8, #n17, #n22 {\n"
"	background-color: rgb(152, 218, 227);\n"
"}\n"
"#n5, #n9, #n13, #n23 {\n"
"	background-color: rgb(248, 187, 212);\n"
"}\n"
"#n6, #n11, #n15 {\n"
"	background-color: rgb(184, 173, 240);\n"
"}QFrame{\n"
"	border-radius: 30px;\n"
"}\n"
"#n1, #n10, #n20, #n18 {\n"
"	background-color: rgb(251, 229, 147);\n"
"}\n"
"#n2, #n7, #n16, #n19 {\n"
"	background-color: rgb(206, 234, 171);\n"
"}\n"
"#n3, #n12, #n14, #n21 {\n"
"	background-color: rgb(254, 178, 135);\n"
"}\n"
"#n4, #n8, #n17, #n22 {\n"
"	background-color: rgb(152, 218, 227);\n"
"}\n"
"#n5, #n9, #n13, #n23 {\n"
"	background-color: rgb(248, 187, 212);\n"
"}\n"
"#n6, #n11, #n15 {\n"
"	background-color: rgb(184, 173, 240);\n"
"}\n"
"QLabel {\n"
"	font: 87 14pt \"Ralewa"
                        "y Black\";\n"
"}\n"
"QPushButton {\n"
"	background: transparent;\n"
"	font: 87 14pt \"Raleway Black\";\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.n16 = QFrame(self.frame)
        self.n16.setObjectName(u"n16")
        self.n16.setCursor(QCursor(Qt.ArrowCursor))
        self.n16.setMouseTracking(True)
        self.n16.setFrameShape(QFrame.Box)
        self.n16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.n16)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(12, 2, 2, 6)
        self.nt16 = QPushButton(self.n16)
        self.nt16.setObjectName(u"nt16")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nt16.sizePolicy().hasHeightForWidth())
        self.nt16.setSizePolicy(sizePolicy)

        self.verticalLayout_23.addWidget(self.nt16)

        self.d16 = QLabel(self.n16)
        self.d16.setObjectName(u"d16")
        self.d16.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d16.setTextFormat(Qt.AutoText)
        self.d16.setScaledContents(True)
        self.d16.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d16.setWordWrap(True)
        self.d16.setOpenExternalLinks(True)
        self.d16.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_23.addWidget(self.d16)


        self.gridLayout.addWidget(self.n16, 2, 3, 1, 1)

        self.n2 = QFrame(self.frame)
        self.n2.setObjectName(u"n2")
        self.n2.setCursor(QCursor(Qt.ArrowCursor))
        self.n2.setMouseTracking(True)
        self.n2.setFrameShape(QFrame.Box)
        self.n2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.n2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(12, 2, 2, 6)
        self.nt2 = QPushButton(self.n2)
        self.nt2.setObjectName(u"nt2")
        sizePolicy.setHeightForWidth(self.nt2.sizePolicy().hasHeightForWidth())
        self.nt2.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.nt2)

        self.d2 = QLabel(self.n2)
        self.d2.setObjectName(u"d2")
        self.d2.setCursor(QCursor(Qt.ArrowCursor))
        self.d2.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d2.setTextFormat(Qt.AutoText)
        self.d2.setScaledContents(True)
        self.d2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d2.setWordWrap(True)
        self.d2.setOpenExternalLinks(True)
        self.d2.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_9.addWidget(self.d2)


        self.gridLayout.addWidget(self.n2, 0, 1, 1, 1)

        self.n10 = QFrame(self.frame)
        self.n10.setObjectName(u"n10")
        self.n10.setCursor(QCursor(Qt.ArrowCursor))
        self.n10.setMouseTracking(True)
        self.n10.setFrameShape(QFrame.Box)
        self.n10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.n10)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(12, 2, 2, 6)
        self.nt10 = QPushButton(self.n10)
        self.nt10.setObjectName(u"nt10")
        sizePolicy.setHeightForWidth(self.nt10.sizePolicy().hasHeightForWidth())
        self.nt10.setSizePolicy(sizePolicy)

        self.verticalLayout_17.addWidget(self.nt10)

        self.d10 = QLabel(self.n10)
        self.d10.setObjectName(u"d10")
        self.d10.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d10.setTextFormat(Qt.AutoText)
        self.d10.setScaledContents(True)
        self.d10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d10.setWordWrap(True)
        self.d10.setOpenExternalLinks(True)
        self.d10.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_17.addWidget(self.d10)


        self.gridLayout.addWidget(self.n10, 1, 3, 1, 1)

        self.n1 = QFrame(self.frame)
        self.n1.setObjectName(u"n1")
        self.n1.setCursor(QCursor(Qt.ArrowCursor))
        self.n1.setMouseTracking(True)
        self.n1.setStyleSheet(u"")
        self.n1.setFrameShape(QFrame.Box)
        self.n1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.n1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(12, 2, 2, 6)
        self.nt1 = QPushButton(self.n1)
        self.nt1.setObjectName(u"nt1")
        sizePolicy.setHeightForWidth(self.nt1.sizePolicy().hasHeightForWidth())
        self.nt1.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.nt1)

        self.d1 = QLabel(self.n1)
        self.d1.setObjectName(u"d1")
        self.d1.setCursor(QCursor(Qt.ArrowCursor))
        self.d1.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d1.setTextFormat(Qt.AutoText)
        self.d1.setScaledContents(True)
        self.d1.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d1.setWordWrap(True)
        self.d1.setOpenExternalLinks(True)
        self.d1.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_8.addWidget(self.d1)


        self.gridLayout.addWidget(self.n1, 0, 0, 1, 1)

        self.n3 = QFrame(self.frame)
        self.n3.setObjectName(u"n3")
        self.n3.setCursor(QCursor(Qt.ArrowCursor))
        self.n3.setMouseTracking(True)
        self.n3.setFrameShape(QFrame.Box)
        self.n3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.n3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(12, 2, 2, 6)
        self.nt3 = QPushButton(self.n3)
        self.nt3.setObjectName(u"nt3")
        sizePolicy.setHeightForWidth(self.nt3.sizePolicy().hasHeightForWidth())
        self.nt3.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.nt3)

        self.d3 = QLabel(self.n3)
        self.d3.setObjectName(u"d3")
        self.d3.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d3.setTextFormat(Qt.AutoText)
        self.d3.setScaledContents(True)
        self.d3.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d3.setWordWrap(True)
        self.d3.setOpenExternalLinks(True)
        self.d3.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_10.addWidget(self.d3)


        self.gridLayout.addWidget(self.n3, 0, 2, 1, 1)

        self.n5 = QFrame(self.frame)
        self.n5.setObjectName(u"n5")
        self.n5.setCursor(QCursor(Qt.ArrowCursor))
        self.n5.setMouseTracking(True)
        self.n5.setFrameShape(QFrame.Box)
        self.n5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.n5)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(12, 2, 2, 6)
        self.nt5 = QPushButton(self.n5)
        self.nt5.setObjectName(u"nt5")
        sizePolicy.setHeightForWidth(self.nt5.sizePolicy().hasHeightForWidth())
        self.nt5.setSizePolicy(sizePolicy)

        self.verticalLayout_12.addWidget(self.nt5)

        self.d5 = QLabel(self.n5)
        self.d5.setObjectName(u"d5")
        self.d5.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d5.setTextFormat(Qt.AutoText)
        self.d5.setScaledContents(True)
        self.d5.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d5.setWordWrap(True)
        self.d5.setOpenExternalLinks(True)
        self.d5.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_12.addWidget(self.d5)


        self.gridLayout.addWidget(self.n5, 0, 4, 1, 1)

        self.n23 = QFrame(self.frame)
        self.n23.setObjectName(u"n23")
        self.n23.setCursor(QCursor(Qt.ArrowCursor))
        self.n23.setMouseTracking(True)
        self.n23.setFrameShape(QFrame.Box)
        self.n23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.n23)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(12, 2, 2, 6)
        self.nt23 = QPushButton(self.n23)
        self.nt23.setObjectName(u"nt23")
        sizePolicy.setHeightForWidth(self.nt23.sizePolicy().hasHeightForWidth())
        self.nt23.setSizePolicy(sizePolicy)

        self.verticalLayout_30.addWidget(self.nt23)

        self.d23 = QLabel(self.n23)
        self.d23.setObjectName(u"d23")
        self.d23.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d23.setTextFormat(Qt.AutoText)
        self.d23.setScaledContents(True)
        self.d23.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d23.setWordWrap(True)
        self.d23.setOpenExternalLinks(True)
        self.d23.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_30.addWidget(self.d23)


        self.gridLayout.addWidget(self.n23, 3, 4, 1, 1)

        self.n11 = QFrame(self.frame)
        self.n11.setObjectName(u"n11")
        self.n11.setCursor(QCursor(Qt.ArrowCursor))
        self.n11.setMouseTracking(True)
        self.n11.setFrameShape(QFrame.Box)
        self.n11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.n11)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(12, 2, 2, 6)
        self.nt11 = QPushButton(self.n11)
        self.nt11.setObjectName(u"nt11")
        sizePolicy.setHeightForWidth(self.nt11.sizePolicy().hasHeightForWidth())
        self.nt11.setSizePolicy(sizePolicy)

        self.verticalLayout_18.addWidget(self.nt11)

        self.d11 = QLabel(self.n11)
        self.d11.setObjectName(u"d11")
        self.d11.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d11.setTextFormat(Qt.AutoText)
        self.d11.setScaledContents(True)
        self.d11.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d11.setWordWrap(True)
        self.d11.setOpenExternalLinks(True)
        self.d11.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_18.addWidget(self.d11)


        self.gridLayout.addWidget(self.n11, 1, 4, 1, 1)

        self.n6 = QFrame(self.frame)
        self.n6.setObjectName(u"n6")
        self.n6.setCursor(QCursor(Qt.ArrowCursor))
        self.n6.setMouseTracking(True)
        self.n6.setFrameShape(QFrame.Box)
        self.n6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.n6)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(12, 2, 2, 6)
        self.nt6 = QPushButton(self.n6)
        self.nt6.setObjectName(u"nt6")
        sizePolicy.setHeightForWidth(self.nt6.sizePolicy().hasHeightForWidth())
        self.nt6.setSizePolicy(sizePolicy)

        self.verticalLayout_13.addWidget(self.nt6)

        self.d6 = QLabel(self.n6)
        self.d6.setObjectName(u"d6")
        self.d6.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d6.setTextFormat(Qt.AutoText)
        self.d6.setScaledContents(True)
        self.d6.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d6.setWordWrap(True)
        self.d6.setOpenExternalLinks(True)
        self.d6.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_13.addWidget(self.d6)


        self.gridLayout.addWidget(self.n6, 0, 5, 1, 1)

        self.n22 = QFrame(self.frame)
        self.n22.setObjectName(u"n22")
        self.n22.setCursor(QCursor(Qt.ArrowCursor))
        self.n22.setMouseTracking(True)
        self.n22.setFrameShape(QFrame.Box)
        self.n22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.n22)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(12, 2, 2, 6)
        self.nt22 = QPushButton(self.n22)
        self.nt22.setObjectName(u"nt22")
        sizePolicy.setHeightForWidth(self.nt22.sizePolicy().hasHeightForWidth())
        self.nt22.setSizePolicy(sizePolicy)

        self.verticalLayout_29.addWidget(self.nt22)

        self.d22 = QLabel(self.n22)
        self.d22.setObjectName(u"d22")
        self.d22.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d22.setTextFormat(Qt.AutoText)
        self.d22.setScaledContents(True)
        self.d22.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d22.setWordWrap(True)
        self.d22.setOpenExternalLinks(True)
        self.d22.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_29.addWidget(self.d22)


        self.gridLayout.addWidget(self.n22, 3, 3, 1, 1)

        self.n12 = QFrame(self.frame)
        self.n12.setObjectName(u"n12")
        self.n12.setCursor(QCursor(Qt.ArrowCursor))
        self.n12.setMouseTracking(True)
        self.n12.setFrameShape(QFrame.Box)
        self.n12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.n12)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(12, 2, 2, 6)
        self.nt12 = QPushButton(self.n12)
        self.nt12.setObjectName(u"nt12")
        sizePolicy.setHeightForWidth(self.nt12.sizePolicy().hasHeightForWidth())
        self.nt12.setSizePolicy(sizePolicy)

        self.verticalLayout_19.addWidget(self.nt12)

        self.d12 = QLabel(self.n12)
        self.d12.setObjectName(u"d12")
        self.d12.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d12.setTextFormat(Qt.AutoText)
        self.d12.setScaledContents(True)
        self.d12.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d12.setWordWrap(True)
        self.d12.setOpenExternalLinks(True)
        self.d12.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_19.addWidget(self.d12)


        self.gridLayout.addWidget(self.n12, 1, 5, 1, 1)

        self.n17 = QFrame(self.frame)
        self.n17.setObjectName(u"n17")
        self.n17.setCursor(QCursor(Qt.ArrowCursor))
        self.n17.setMouseTracking(True)
        self.n17.setFrameShape(QFrame.Box)
        self.n17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.n17)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(12, 2, 2, 6)
        self.nt17 = QPushButton(self.n17)
        self.nt17.setObjectName(u"nt17")
        sizePolicy.setHeightForWidth(self.nt17.sizePolicy().hasHeightForWidth())
        self.nt17.setSizePolicy(sizePolicy)

        self.verticalLayout_24.addWidget(self.nt17)

        self.d17 = QLabel(self.n17)
        self.d17.setObjectName(u"d17")
        self.d17.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d17.setTextFormat(Qt.AutoText)
        self.d17.setScaledContents(True)
        self.d17.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d17.setWordWrap(True)
        self.d17.setOpenExternalLinks(True)
        self.d17.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_24.addWidget(self.d17)


        self.gridLayout.addWidget(self.n17, 2, 4, 1, 1)

        self.n7 = QFrame(self.frame)
        self.n7.setObjectName(u"n7")
        self.n7.setCursor(QCursor(Qt.ArrowCursor))
        self.n7.setMouseTracking(True)
        self.n7.setFrameShape(QFrame.Box)
        self.n7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.n7)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(12, 2, 2, 6)
        self.nt7 = QPushButton(self.n7)
        self.nt7.setObjectName(u"nt7")
        sizePolicy.setHeightForWidth(self.nt7.sizePolicy().hasHeightForWidth())
        self.nt7.setSizePolicy(sizePolicy)

        self.verticalLayout_14.addWidget(self.nt7)

        self.d7 = QLabel(self.n7)
        self.d7.setObjectName(u"d7")
        self.d7.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d7.setTextFormat(Qt.AutoText)
        self.d7.setScaledContents(True)
        self.d7.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d7.setWordWrap(True)
        self.d7.setOpenExternalLinks(True)
        self.d7.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_14.addWidget(self.d7)


        self.gridLayout.addWidget(self.n7, 1, 0, 1, 1)

        self.addBtnFrame = QFrame(self.frame)
        self.addBtnFrame.setObjectName(u"addBtnFrame")
        self.addBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.addBtnFrame.setFrameShadow(QFrame.Raised)
        self.addBtn = QPushButton(self.addBtnFrame)
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setGeometry(QRect(15, 10, 64, 64))
        self.addBtn.setMaximumSize(QSize(64, 64))
        self.addBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addBtn.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"height: 64px;\n"
"width: 64px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"../../TFG/icon pack/ADD.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addBtn.setIcon(icon10)
        self.addBtn.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.addBtnFrame, 3, 5, 1, 1)

        self.n21 = QFrame(self.frame)
        self.n21.setObjectName(u"n21")
        self.n21.setCursor(QCursor(Qt.ArrowCursor))
        self.n21.setMouseTracking(True)
        self.n21.setFrameShape(QFrame.Box)
        self.n21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.n21)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(12, 2, 2, 6)
        self.nt21 = QPushButton(self.n21)
        self.nt21.setObjectName(u"nt21")
        sizePolicy.setHeightForWidth(self.nt21.sizePolicy().hasHeightForWidth())
        self.nt21.setSizePolicy(sizePolicy)

        self.verticalLayout_28.addWidget(self.nt21)

        self.d21 = QLabel(self.n21)
        self.d21.setObjectName(u"d21")
        self.d21.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d21.setTextFormat(Qt.AutoText)
        self.d21.setScaledContents(True)
        self.d21.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d21.setWordWrap(True)
        self.d21.setOpenExternalLinks(True)
        self.d21.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_28.addWidget(self.d21)


        self.gridLayout.addWidget(self.n21, 3, 2, 1, 1)

        self.n18 = QFrame(self.frame)
        self.n18.setObjectName(u"n18")
        self.n18.setCursor(QCursor(Qt.ArrowCursor))
        self.n18.setMouseTracking(True)
        self.n18.setFrameShape(QFrame.Box)
        self.n18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.n18)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(12, 2, 2, 6)
        self.nt18 = QPushButton(self.n18)
        self.nt18.setObjectName(u"nt18")
        sizePolicy.setHeightForWidth(self.nt18.sizePolicy().hasHeightForWidth())
        self.nt18.setSizePolicy(sizePolicy)

        self.verticalLayout_25.addWidget(self.nt18)

        self.d18 = QLabel(self.n18)
        self.d18.setObjectName(u"d18")
        self.d18.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d18.setTextFormat(Qt.AutoText)
        self.d18.setScaledContents(True)
        self.d18.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d18.setWordWrap(True)
        self.d18.setOpenExternalLinks(True)
        self.d18.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_25.addWidget(self.d18)


        self.gridLayout.addWidget(self.n18, 2, 5, 1, 1)

        self.n13 = QFrame(self.frame)
        self.n13.setObjectName(u"n13")
        self.n13.setCursor(QCursor(Qt.ArrowCursor))
        self.n13.setMouseTracking(True)
        self.n13.setFrameShape(QFrame.Box)
        self.n13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.n13)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(12, 2, 2, 6)
        self.nt13 = QPushButton(self.n13)
        self.nt13.setObjectName(u"nt13")
        sizePolicy.setHeightForWidth(self.nt13.sizePolicy().hasHeightForWidth())
        self.nt13.setSizePolicy(sizePolicy)

        self.verticalLayout_20.addWidget(self.nt13)

        self.d13 = QLabel(self.n13)
        self.d13.setObjectName(u"d13")
        self.d13.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d13.setTextFormat(Qt.AutoText)
        self.d13.setScaledContents(True)
        self.d13.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d13.setWordWrap(True)
        self.d13.setOpenExternalLinks(True)
        self.d13.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_20.addWidget(self.d13)


        self.gridLayout.addWidget(self.n13, 2, 0, 1, 1)

        self.n8 = QFrame(self.frame)
        self.n8.setObjectName(u"n8")
        self.n8.setCursor(QCursor(Qt.ArrowCursor))
        self.n8.setMouseTracking(True)
        self.n8.setFrameShape(QFrame.Box)
        self.n8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.n8)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(12, 2, 2, 6)
        self.nt8 = QPushButton(self.n8)
        self.nt8.setObjectName(u"nt8")
        sizePolicy.setHeightForWidth(self.nt8.sizePolicy().hasHeightForWidth())
        self.nt8.setSizePolicy(sizePolicy)

        self.verticalLayout_15.addWidget(self.nt8)

        self.d8 = QLabel(self.n8)
        self.d8.setObjectName(u"d8")
        self.d8.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d8.setTextFormat(Qt.AutoText)
        self.d8.setScaledContents(True)
        self.d8.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d8.setWordWrap(True)
        self.d8.setOpenExternalLinks(True)
        self.d8.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_15.addWidget(self.d8)


        self.gridLayout.addWidget(self.n8, 1, 1, 1, 1)

        self.n15 = QFrame(self.frame)
        self.n15.setObjectName(u"n15")
        self.n15.setCursor(QCursor(Qt.ArrowCursor))
        self.n15.setMouseTracking(True)
        self.n15.setFrameShape(QFrame.Box)
        self.n15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.n15)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(12, 2, 2, 6)
        self.nt15 = QPushButton(self.n15)
        self.nt15.setObjectName(u"nt15")
        sizePolicy.setHeightForWidth(self.nt15.sizePolicy().hasHeightForWidth())
        self.nt15.setSizePolicy(sizePolicy)

        self.verticalLayout_22.addWidget(self.nt15)

        self.d15 = QLabel(self.n15)
        self.d15.setObjectName(u"d15")
        self.d15.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d15.setTextFormat(Qt.AutoText)
        self.d15.setScaledContents(True)
        self.d15.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d15.setWordWrap(True)
        self.d15.setOpenExternalLinks(True)
        self.d15.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_22.addWidget(self.d15)


        self.gridLayout.addWidget(self.n15, 2, 2, 1, 1)

        self.n20 = QFrame(self.frame)
        self.n20.setObjectName(u"n20")
        self.n20.setCursor(QCursor(Qt.ArrowCursor))
        self.n20.setMouseTracking(True)
        self.n20.setFrameShape(QFrame.Box)
        self.n20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.n20)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(12, 2, 2, 6)
        self.nt20 = QPushButton(self.n20)
        self.nt20.setObjectName(u"nt20")
        sizePolicy.setHeightForWidth(self.nt20.sizePolicy().hasHeightForWidth())
        self.nt20.setSizePolicy(sizePolicy)

        self.verticalLayout_27.addWidget(self.nt20)

        self.d20 = QLabel(self.n20)
        self.d20.setObjectName(u"d20")
        self.d20.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d20.setTextFormat(Qt.AutoText)
        self.d20.setScaledContents(True)
        self.d20.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d20.setWordWrap(True)
        self.d20.setOpenExternalLinks(True)
        self.d20.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_27.addWidget(self.d20)


        self.gridLayout.addWidget(self.n20, 3, 1, 1, 1)

        self.n4 = QFrame(self.frame)
        self.n4.setObjectName(u"n4")
        self.n4.setCursor(QCursor(Qt.ArrowCursor))
        self.n4.setMouseTracking(True)
        self.n4.setFrameShape(QFrame.Box)
        self.n4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.n4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(12, 2, 2, 6)
        self.nt4 = QPushButton(self.n4)
        self.nt4.setObjectName(u"nt4")
        sizePolicy.setHeightForWidth(self.nt4.sizePolicy().hasHeightForWidth())
        self.nt4.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.nt4)

        self.d4 = QLabel(self.n4)
        self.d4.setObjectName(u"d4")
        self.d4.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d4.setTextFormat(Qt.AutoText)
        self.d4.setScaledContents(True)
        self.d4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d4.setWordWrap(True)
        self.d4.setOpenExternalLinks(True)
        self.d4.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_11.addWidget(self.d4)


        self.gridLayout.addWidget(self.n4, 0, 3, 1, 1)

        self.n19 = QFrame(self.frame)
        self.n19.setObjectName(u"n19")
        self.n19.setCursor(QCursor(Qt.ArrowCursor))
        self.n19.setMouseTracking(True)
        self.n19.setFrameShape(QFrame.Box)
        self.n19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.n19)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(12, 2, 2, 6)
        self.nt19 = QPushButton(self.n19)
        self.nt19.setObjectName(u"nt19")
        sizePolicy.setHeightForWidth(self.nt19.sizePolicy().hasHeightForWidth())
        self.nt19.setSizePolicy(sizePolicy)

        self.verticalLayout_26.addWidget(self.nt19)

        self.d19 = QLabel(self.n19)
        self.d19.setObjectName(u"d19")
        self.d19.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d19.setTextFormat(Qt.AutoText)
        self.d19.setScaledContents(True)
        self.d19.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d19.setWordWrap(True)
        self.d19.setOpenExternalLinks(True)
        self.d19.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_26.addWidget(self.d19)


        self.gridLayout.addWidget(self.n19, 3, 0, 1, 1)

        self.n9 = QFrame(self.frame)
        self.n9.setObjectName(u"n9")
        self.n9.setCursor(QCursor(Qt.ArrowCursor))
        self.n9.setMouseTracking(True)
        self.n9.setFrameShape(QFrame.Box)
        self.n9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.n9)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(12, 2, 2, 6)
        self.nt9 = QPushButton(self.n9)
        self.nt9.setObjectName(u"nt9")
        sizePolicy.setHeightForWidth(self.nt9.sizePolicy().hasHeightForWidth())
        self.nt9.setSizePolicy(sizePolicy)

        self.verticalLayout_16.addWidget(self.nt9)

        self.d9 = QLabel(self.n9)
        self.d9.setObjectName(u"d9")
        self.d9.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d9.setTextFormat(Qt.AutoText)
        self.d9.setScaledContents(True)
        self.d9.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d9.setWordWrap(True)
        self.d9.setOpenExternalLinks(True)
        self.d9.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_16.addWidget(self.d9)


        self.gridLayout.addWidget(self.n9, 1, 2, 1, 1)

        self.n14 = QFrame(self.frame)
        self.n14.setObjectName(u"n14")
        self.n14.setCursor(QCursor(Qt.ArrowCursor))
        self.n14.setMouseTracking(True)
        self.n14.setFrameShape(QFrame.Box)
        self.n14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.n14)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(12, 2, 2, 6)
        self.nt14 = QPushButton(self.n14)
        self.nt14.setObjectName(u"nt14")
        sizePolicy.setHeightForWidth(self.nt14.sizePolicy().hasHeightForWidth())
        self.nt14.setSizePolicy(sizePolicy)

        self.verticalLayout_21.addWidget(self.nt14)

        self.d14 = QLabel(self.n14)
        self.d14.setObjectName(u"d14")
        self.d14.setStyleSheet(u"font: 0 italic 12pt \"Raleway Thin\";")
        self.d14.setTextFormat(Qt.AutoText)
        self.d14.setScaledContents(True)
        self.d14.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.d14.setWordWrap(True)
        self.d14.setOpenExternalLinks(True)
        self.d14.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.verticalLayout_21.addWidget(self.d14)


        self.gridLayout.addWidget(self.n14, 2, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)

        self.stackedWidget.addWidget(self.p_Inicio)
        self.p_NoteDetails = QWidget()
        self.p_NoteDetails.setObjectName(u"p_NoteDetails")
        self.verticalLayout_35 = QVBoxLayout(self.p_NoteDetails)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.p_NoteDetails)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 200))
        self.frame_10.setMaximumSize(QSize(16777215, 200))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_10)
        self.verticalLayout_37.setSpacing(6)
        self.verticalLayout_37.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(25, -1, -1, -1)
        self.viewTitle = QLabel(self.frame_10)
        self.viewTitle.setObjectName(u"viewTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewTitle.sizePolicy().hasHeightForWidth())
        self.viewTitle.setSizePolicy(sizePolicy1)
        self.viewTitle.setStyleSheet(u"font: 63 30pt \"Raleway SemiBold\";")
        self.viewTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.viewTitle.setWordWrap(True)

        self.verticalLayout_37.addWidget(self.viewTitle)


        self.verticalLayout_35.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.p_NoteDetails)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setSpacing(15)
        self.horizontalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(25, 0, 25, 0)
        self.viewContent = QTextBrowser(self.frame_11)
        self.viewContent.setObjectName(u"viewContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.viewContent.sizePolicy().hasHeightForWidth())
        self.viewContent.setSizePolicy(sizePolicy2)
        self.viewContent.setMinimumSize(QSize(800, 400))
        self.viewContent.setStyleSheet(u"QTextEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
"}")

        self.horizontalLayout_11.addWidget(self.viewContent)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"font: 63 italic 12pt \"Raleway SemiBold\";")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_13)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.viewCreator = QLabel(self.frame_13)
        self.viewCreator.setObjectName(u"viewCreator")

        self.verticalLayout_36.addWidget(self.viewCreator)

        self.viewOriginDate = QLabel(self.frame_13)
        self.viewOriginDate.setObjectName(u"viewOriginDate")

        self.verticalLayout_36.addWidget(self.viewOriginDate)

        self.viewLastEdit = QLabel(self.frame_13)
        self.viewLastEdit.setObjectName(u"viewLastEdit")

        self.verticalLayout_36.addWidget(self.viewLastEdit)


        self.horizontalLayout_11.addWidget(self.frame_13)


        self.verticalLayout_35.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.p_NoteDetails)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 150))
        self.frame_12.setMaximumSize(QSize(16777215, 150))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.goBackBttn = QPushButton(self.frame_12)
        self.goBackBttn.setObjectName(u"goBackBttn")
        self.goBackBttn.setStyleSheet(u"background: transparent;\n"
"font: 12pt \"Geomanist\";")
        icon11 = QIcon()
        icon11.addFile(u"icon pack/ATRAS.png", QSize(), QIcon.Normal, QIcon.Off)
        self.goBackBttn.setIcon(icon11)
        self.goBackBttn.setIconSize(QSize(36, 36))

        self.horizontalLayout_12.addWidget(self.goBackBttn)

        self.horizontalSpacer_6 = QSpacerItem(975, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)


        self.verticalLayout_35.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.p_NoteDetails)
        self.p_AddNote = QWidget()
        self.p_AddNote.setObjectName(u"p_AddNote")
        self.verticalLayout_5 = QVBoxLayout(self.p_AddNote)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_userBttn = QFrame(self.p_AddNote)
        self.frame_userBttn.setObjectName(u"frame_userBttn")
        self.frame_userBttn.setMaximumSize(QSize(16777215, 70))
        self.frame_userBttn.setStyleSheet(u"")
        self.frame_userBttn.setFrameShape(QFrame.StyledPanel)
        self.frame_userBttn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_userBttn)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 5, 20, 0)
        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.usrBttn = QPushButton(self.frame_userBttn)
        self.usrBttn.setObjectName(u"usrBttn")
        self.usrBttn.setMinimumSize(QSize(100, 50))
        self.usrBttn.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(144, 202, 249);\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border-radius: 25px;\n"
"	padding: 10px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"../../TFG/icon pack/USER.png", QSize(), QIcon.Normal, QIcon.Off)
        self.usrBttn.setIcon(icon12)
        self.usrBttn.setIconSize(QSize(36, 36))

        self.horizontalLayout_3.addWidget(self.usrBttn)


        self.verticalLayout_5.addWidget(self.frame_userBttn)

        self.frame_contenido = QFrame(self.p_AddNote)
        self.frame_contenido.setObjectName(u"frame_contenido")
        self.frame_contenido.setMaximumSize(QSize(16777215, 16777215))
        self.frame_contenido.setStyleSheet(u"")
        self.frame_contenido.setFrameShape(QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_contenido)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(30, 0, 0, 0)
        self.lbl_Titulo = QLabel(self.frame_contenido)
        self.lbl_Titulo.setObjectName(u"lbl_Titulo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_Titulo.sizePolicy().hasHeightForWidth())
        self.lbl_Titulo.setSizePolicy(sizePolicy3)
        self.lbl_Titulo.setMinimumSize(QSize(80, 50))
        self.lbl_Titulo.setStyleSheet(u"font: 81 25pt \"Raleway ExtraBold\";")
        self.lbl_Titulo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.lbl_Titulo)

        self.inpTitulo = QLineEdit(self.frame_contenido)
        self.inpTitulo.setObjectName(u"inpTitulo")
        self.inpTitulo.setMaximumSize(QSize(244, 16777215))
        self.inpTitulo.setStyleSheet(u"QLineEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
" max-width: 190px;\n"
"}\n"
"\n"
"")
        self.inpTitulo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.inpTitulo)

        self.lbl_Desc = QLabel(self.frame_contenido)
        self.lbl_Desc.setObjectName(u"lbl_Desc")
        sizePolicy3.setHeightForWidth(self.lbl_Desc.sizePolicy().hasHeightForWidth())
        self.lbl_Desc.setSizePolicy(sizePolicy3)
        self.lbl_Desc.setStyleSheet(u"font: 81 25pt \"Raleway ExtraBold\";")
        self.lbl_Desc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_6.addWidget(self.lbl_Desc)

        self.inpDesc = QTextEdit(self.frame_contenido)
        self.inpDesc.setObjectName(u"inpDesc")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.inpDesc.sizePolicy().hasHeightForWidth())
        self.inpDesc.setSizePolicy(sizePolicy4)
        self.inpDesc.setMaximumSize(QSize(800, 800))
        self.inpDesc.setStyleSheet(u"QTextEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
"}\n"
"\n"
"")

        self.verticalLayout_6.addWidget(self.inpDesc)

        self.frame_2 = QFrame(self.frame_contenido)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 30, 20, 0)
        self.dateLabel = QLabel(self.frame_2)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setStyleSheet(u"font: 63 italic 12pt \"Raleway SemiBold\";")
        self.dateLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_8.addWidget(self.dateLabel)

        self.horizontalSpacer_7 = QSpacerItem(484, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.cancelBttn_5 = QPushButton(self.frame_2)
        self.cancelBttn_5.setObjectName(u"cancelBttn_5")
        self.cancelBttn_5.setMinimumSize(QSize(120, 64))
        self.cancelBttn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBttn_5.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(251, 145, 152);\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(230, 133, 139);\n"
"}")
        self.cancelBttn_5.setIcon(icon4)
        self.cancelBttn_5.setIconSize(QSize(36, 36))

        self.horizontalLayout_8.addWidget(self.cancelBttn_5)

        self.saveBttn_5 = QPushButton(self.frame_2)
        self.saveBttn_5.setObjectName(u"saveBttn_5")
        self.saveBttn_5.setMinimumSize(QSize(120, 64))
        self.saveBttn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.saveBttn_5.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(167, 196, 238);	\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(157, 184, 223);\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"../../TFG/icon pack/SAVE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveBttn_5.setIcon(icon13)
        self.saveBttn_5.setIconSize(QSize(36, 36))

        self.horizontalLayout_8.addWidget(self.saveBttn_5)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_5.addWidget(self.frame_contenido)

        self.stackedWidget.addWidget(self.p_AddNote)
        self.p_Busqueda = QWidget()
        self.p_Busqueda.setObjectName(u"p_Busqueda")
        self.p_Busqueda.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout_7 = QVBoxLayout(self.p_Busqueda)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.p_Busqueda)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setMaximumSize(QSize(16777215, 250))
        self.frame_3.setLayoutDirection(Qt.LeftToRight)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(8, 10, 20, 0)
        self.fil_Title = QLineEdit(self.frame_3)
        self.fil_Title.setObjectName(u"fil_Title")
        self.fil_Title.setMaximumSize(QSize(244, 16777215))
        self.fil_Title.setStyleSheet(u"QLineEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
" max-width: 190px;\n"
"}\n"
"\n"
"")
        self.fil_Title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_9.addWidget(self.fil_Title)

        self.horizontalSpacer_8 = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.filterButton = QPushButton(self.frame_3)
        self.filterButton.setObjectName(u"filterButton")
        self.filterButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.filterButton.setStyleSheet(u"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 5px 15px;\n"
" background: white;\n"
"")

        self.horizontalLayout_9.addWidget(self.filterButton)


        self.verticalLayout_7.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frameResultados = QFrame(self.p_Busqueda)
        self.frameResultados.setObjectName(u"frameResultados")
        sizePolicy1.setHeightForWidth(self.frameResultados.sizePolicy().hasHeightForWidth())
        self.frameResultados.setSizePolicy(sizePolicy1)
        self.frameResultados.setStyleSheet(u"")
        self.frameResultados.setFrameShape(QFrame.StyledPanel)
        self.frameResultados.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frameResultados)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tablaResultados = QTableWidget(self.frameResultados)
        if (self.tablaResultados.columnCount() < 4):
            self.tablaResultados.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaResultados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tablaResultados.setObjectName(u"tablaResultados")
        self.tablaResultados.setStyleSheet(u"QTableWidget{\n"
"	gridline-color: rgb(0,206,151);\n"
"	color: #000000;\n"
"	font-size: 12pt;\n"
"}\n"
"QHeaderView::section {\n"
"	\n"
"	background-color: rgb(182, 207, 242);\n"
"	border: 1px solid rgb(0, 0, 0);\n"
"	font-size: 12pt;\n"
"}\n"
"QTableWidget QTableCorenerButton::section {\n"
"	background-color: rgb(0,0,0);\n"
"	border: 1px solid rgb(0,206,151)\n"
"}")
        self.tablaResultados.setAlternatingRowColors(True)
        self.tablaResultados.setSortingEnabled(True)
        self.tablaResultados.setWordWrap(True)
        self.tablaResultados.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaResultados.horizontalHeader().setProperty("showSortIndicator", True)
        self.tablaResultados.verticalHeader().setCascadingSectionResizes(False)
        self.tablaResultados.verticalHeader().setProperty("showSortIndicator", False)
        self.tablaResultados.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_4.addWidget(self.tablaResultados)


        self.verticalLayout_7.addWidget(self.frameResultados)

        self.stackedWidget.addWidget(self.p_Busqueda)
        self.p_Edicion = QWidget()
        self.p_Edicion.setObjectName(u"p_Edicion")
        self.verticalLayout_33 = QVBoxLayout(self.p_Edicion)
        self.verticalLayout_33.setSpacing(6)
        self.verticalLayout_33.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_7 = QFrame(self.p_Edicion)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 70))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.editNoteId = QLineEdit(self.frame_7)
        self.editNoteId.setObjectName(u"editNoteId")
        self.editNoteId.setMaximumSize(QSize(244, 16777215))
        self.editNoteId.setStyleSheet(u"QLineEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
" max-width: 190px;\n"
"}\n"
"\n"
"")
        self.editNoteId.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_6.addWidget(self.editNoteId)

        self.horizontalSpacer_4 = QSpacerItem(701, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.searchButton_edit = QPushButton(self.frame_7)
        self.searchButton_edit.setObjectName(u"searchButton_edit")
        self.searchButton_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_edit.setStyleSheet(u"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 5px 15px;\n"
" background: white;\n"
"")

        self.horizontalLayout_6.addWidget(self.searchButton_edit)


        self.verticalLayout_33.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.p_Edicion)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_8)
        self.verticalLayout_34.setSpacing(40)
        self.verticalLayout_34.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(30, 20, -1, -1)
        self.inpTitulo_2 = QLineEdit(self.frame_8)
        self.inpTitulo_2.setObjectName(u"inpTitulo_2")
        self.inpTitulo_2.setMaximumSize(QSize(244, 16777215))
        self.inpTitulo_2.setStyleSheet(u"QLineEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
" max-width: 190px;\n"
"}\n"
"\n"
"")
        self.inpTitulo_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_34.addWidget(self.inpTitulo_2)

        self.inpDesc_2 = QTextEdit(self.frame_8)
        self.inpDesc_2.setObjectName(u"inpDesc_2")
        sizePolicy4.setHeightForWidth(self.inpDesc_2.sizePolicy().hasHeightForWidth())
        self.inpDesc_2.setSizePolicy(sizePolicy4)
        self.inpDesc_2.setMaximumSize(QSize(800, 800))
        self.inpDesc_2.setStyleSheet(u"QTextEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
"}\n"
"\n"
"")

        self.verticalLayout_34.addWidget(self.inpDesc_2)


        self.verticalLayout_33.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.p_Edicion)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 200))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(801, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.cancelBttn_9 = QPushButton(self.frame_9)
        self.cancelBttn_9.setObjectName(u"cancelBttn_9")
        self.cancelBttn_9.setMinimumSize(QSize(120, 64))
        self.cancelBttn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBttn_9.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(251, 145, 152);\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(230, 133, 139);\n"
"}")
        self.cancelBttn_9.setIcon(icon4)
        self.cancelBttn_9.setIconSize(QSize(36, 36))

        self.horizontalLayout_7.addWidget(self.cancelBttn_9)

        self.updateNoteBttn = QPushButton(self.frame_9)
        self.updateNoteBttn.setObjectName(u"updateNoteBttn")
        self.updateNoteBttn.setMinimumSize(QSize(120, 64))
        self.updateNoteBttn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateNoteBttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(167, 196, 238);	\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(157, 184, 223);\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"icon pack/SAVE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.updateNoteBttn.setIcon(icon14)
        self.updateNoteBttn.setIconSize(QSize(36, 36))

        self.horizontalLayout_7.addWidget(self.updateNoteBttn)


        self.verticalLayout_33.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.p_Edicion)
        self.p_Borrado = QWidget()
        self.p_Borrado.setObjectName(u"p_Borrado")
        self.verticalLayout_31 = QVBoxLayout(self.p_Borrado)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.p_Borrado)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setEnabled(True)
        self.frame_4.setMaximumSize(QSize(16777215, 250))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(8, 10, 20, 0)
        self.deleteNoteId = QLineEdit(self.frame_4)
        self.deleteNoteId.setObjectName(u"deleteNoteId")
        self.deleteNoteId.setMaximumSize(QSize(244, 16777215))
        self.deleteNoteId.setStyleSheet(u"QLineEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
" max-width: 190px;\n"
"}\n"
"\n"
"")
        self.deleteNoteId.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_10.addWidget(self.deleteNoteId)

        self.horizontalSpacer_9 = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.searchButton_delete = QPushButton(self.frame_4)
        self.searchButton_delete.setObjectName(u"searchButton_delete")
        self.searchButton_delete.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton_delete.setStyleSheet(u"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 5px 15px;\n"
" background: white;\n"
"")

        self.horizontalLayout_10.addWidget(self.searchButton_delete)


        self.verticalLayout_31.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.p_Borrado)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_5)
        self.verticalLayout_32.setSpacing(40)
        self.verticalLayout_32.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(30, -1, 30, 20)
        self.tituloBorrado = QLabel(self.frame_5)
        self.tituloBorrado.setObjectName(u"tituloBorrado")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tituloBorrado.sizePolicy().hasHeightForWidth())
        self.tituloBorrado.setSizePolicy(sizePolicy5)
        self.tituloBorrado.setMaximumSize(QSize(16777215, 80))
        self.tituloBorrado.setStyleSheet(u"font: 81 25pt \"Raleway ExtraBold\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
"")
        self.tituloBorrado.setWordWrap(True)

        self.verticalLayout_32.addWidget(self.tituloBorrado)

        self.contenidoBorrado = QTextBrowser(self.frame_5)
        self.contenidoBorrado.setObjectName(u"contenidoBorrado")
        self.contenidoBorrado.setStyleSheet(u"QTextEdit {\n"
"font: 57 14pt \"Raleway Medium\";\n"
" border: 2px solid #8707ff;\n"
" border-radius: 10px;\n"
" padding: 10px 25px;\n"
" background: transparent;\n"
"}")
        self.contenidoBorrado.setReadOnly(True)

        self.verticalLayout_32.addWidget(self.contenidoBorrado)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMaximumSize(QSize(16777215, 150))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(757, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.cancelBttn_8 = QPushButton(self.frame_6)
        self.cancelBttn_8.setObjectName(u"cancelBttn_8")
        self.cancelBttn_8.setMinimumSize(QSize(120, 64))
        self.cancelBttn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelBttn_8.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(251, 145, 152);\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(230, 133, 139);\n"
"}")
        self.cancelBttn_8.setIcon(icon4)
        self.cancelBttn_8.setIconSize(QSize(36, 36))

        self.horizontalLayout_5.addWidget(self.cancelBttn_8)

        self.deleteNoteBttn = QPushButton(self.frame_6)
        self.deleteNoteBttn.setObjectName(u"deleteNoteBttn")
        self.deleteNoteBttn.setMinimumSize(QSize(120, 64))
        self.deleteNoteBttn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteNoteBttn.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(167, 196, 238);	\n"
"	font: 57 10pt \"Raleway Medium\";\n"
"	border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(157, 184, 223);\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"icon pack/DELETE_bttn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteNoteBttn.setIcon(icon15)
        self.deleteNoteBttn.setIconSize(QSize(36, 36))

        self.horizontalLayout_5.addWidget(self.deleteNoteBttn)


        self.verticalLayout_32.addWidget(self.frame_6)


        self.verticalLayout_31.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.p_Borrado)
        self.p_Ayuda = QWidget()
        self.p_Ayuda.setObjectName(u"p_Ayuda")
        self.pushButton_5 = QPushButton(self.p_Ayuda)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(470, 290, 75, 23))
        self.stackedWidget.addWidget(self.p_Ayuda)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_ventana)


        self.verticalLayout.addWidget(self.frame_inferior)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.nt1.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(qtTrId(u""))
        self.btnMenu.setText("")
        self.btnMinimizar.setText("")
        self.btnMaximizar.setText("")
        self.btnRestaurar.setText("")
        self.btnCerrar.setText("")
        self.bt_inicio.setText(qtTrId(u""))
        self.bt_Buscar.setText(qtTrId(u""))
        self.bt_Editar.setText(qtTrId(u""))
        self.bt_Borrado.setText(qtTrId(u""))
        self.bt_Ayuda.setText(qtTrId(u""))
        self.madeBy.setText(qtTrId(u""))
        self.nt16.setText("")
        self.d16.setText(qtTrId(u""))
        self.nt2.setText("")
        self.d2.setText(qtTrId(u""))
        self.nt10.setText("")
        self.d10.setText(qtTrId(u""))
        self.nt1.setText("")
        self.d1.setText(qtTrId(u""))
        self.nt3.setText("")
        self.d3.setText(qtTrId(u""))
        self.nt5.setText("")
        self.d5.setText(qtTrId(u""))
        self.nt23.setText("")
        self.d23.setText(qtTrId(u""))
        self.nt11.setText("")
        self.d11.setText(qtTrId(u""))
        self.nt6.setText("")
        self.d6.setText(qtTrId(u""))
        self.nt22.setText("")
        self.d22.setText(qtTrId(u""))
        self.nt12.setText("")
        self.d12.setText(qtTrId(u""))
        self.nt17.setText("")
        self.d17.setText(qtTrId(u""))
        self.nt7.setText("")
        self.d7.setText(qtTrId(u""))
        self.addBtn.setText("")
        self.nt21.setText("")
        self.d21.setText(qtTrId(u""))
        self.nt18.setText("")
        self.d18.setText(qtTrId(u""))
        self.nt13.setText("")
        self.d13.setText(qtTrId(u""))
        self.nt8.setText("")
        self.d8.setText(qtTrId(u""))
        self.nt15.setText("")
        self.d15.setText(qtTrId(u""))
        self.nt20.setText("")
        self.d20.setText(qtTrId(u""))
        self.nt4.setText("")
        self.d4.setText(qtTrId(u""))
        self.nt19.setText("")
        self.d19.setText(qtTrId(u""))
        self.nt9.setText("")
        self.d9.setText(qtTrId(u""))
        self.nt14.setText("")
        self.d14.setText(qtTrId(u""))
        self.viewTitle.setText(qtTrId(u""))
        self.viewContent.setHtml(qtTrId(u""))
        self.viewCreator.setText(qtTrId(u""))
        self.viewOriginDate.setText(qtTrId(u""))
        self.viewLastEdit.setText(qtTrId(u""))
        self.goBackBttn.setText(qtTrId(u""))
        self.usrBttn.setText("")
        self.lbl_Titulo.setText(qtTrId(u""))
        self.lbl_Desc.setText(qtTrId(u""))
        self.inpDesc.setHtml(qtTrId(u""))
        self.dateLabel.setText("")
        self.cancelBttn_5.setText(qtTrId(u""))
        self.saveBttn_5.setText(qtTrId(u""))
        self.fil_Title.setPlaceholderText(qtTrId(u""))
        self.filterButton.setText(qtTrId(u""))
        ___qtablewidgetitem = self.tablaResultados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(qtTrId(u""));
        ___qtablewidgetitem1 = self.tablaResultados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(qtTrId(u""));
        ___qtablewidgetitem2 = self.tablaResultados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(qtTrId(u""));
        ___qtablewidgetitem3 = self.tablaResultados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(qtTrId(u""));
        self.editNoteId.setPlaceholderText(qtTrId(u""))
        self.searchButton_edit.setText(qtTrId(u""))
        self.inpTitulo_2.setText(qtTrId(u""))
        self.inpDesc_2.setHtml(qtTrId(u""))
        self.cancelBttn_9.setText(qtTrId(u""))
        self.updateNoteBttn.setText(qtTrId(u""))
        self.deleteNoteId.setPlaceholderText(qtTrId(u""))
        self.searchButton_delete.setText(qtTrId(u""))
        self.tituloBorrado.setText(qtTrId(u""))
        self.cancelBttn_8.setText(qtTrId(u""))
        self.deleteNoteBttn.setText(qtTrId(u""))
        self.pushButton_5.setText(qtTrId(u""))
    # retranslateUi

