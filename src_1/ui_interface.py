# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomCheckBox import QCustomCheckBox
from Custom_Widgets.Theme import QPushButton
from Custom_Widgets.Theme import QLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(265, 380)
        MainWindow.setMaximumSize(QSize(500, 500))
        MainWindow.setStyleSheet(u"background:#444d4d")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background:white\n"
"")
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer = QSpacerItem(167, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.minimize_window_button = QPushButton(self.widget)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimize_window_button.sizePolicy().hasHeightForWidth())
        self.minimize_window_button.setSizePolicy(sizePolicy)
        self.minimize_window_button.setMinimumSize(QSize(17, 19))
        self.minimize_window_button.setMaximumSize(QSize(17, 19))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/window_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon)
        self.minimize_window_button.setIconSize(QSize(13, 13))

        self.gridLayout_7.addWidget(self.minimize_window_button, 0, 0, 1, 1)

        self.restore_window_button = QPushButton(self.widget)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMinimumSize(QSize(17, 19))
        self.restore_window_button.setMaximumSize(QSize(17, 19))
        icon1 = QIcon()
        icon1.addFile(u":/feather/icons/feather/maximize-2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon1)
        self.restore_window_button.setIconSize(QSize(10, 26))

        self.gridLayout_7.addWidget(self.restore_window_button, 0, 1, 1, 1)

        self.close_window_button = QPushButton(self.widget)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(17, 19))
        self.close_window_button.setMaximumSize(QSize(17, 19))
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/window_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon2)
        self.close_window_button.setIconSize(QSize(10, 13))

        self.gridLayout_7.addWidget(self.close_window_button, 0, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 1, 1, 1)

        self.stackedWidget = QCustomQStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: white;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(16, 9, 10, 4)
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(177, 30))
        self.lineEdit_2.setMaximumSize(QSize(177, 30))
        self.lineEdit_2.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #ffffff;\n"
"                padding: 6px;\n"
"                border-radius: 6px;\n"
"                background-color: #ffffff;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(177, 0))
        self.lineEdit.setMaximumSize(QSize(177, 16777215))
        self.lineEdit.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #ffffff;\n"
"                padding: 6px;\n"
"                border-radius: 6px;\n"
"                background-color: #ffffff;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.lineEdit.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEdit)


        self.gridLayout_3.addLayout(self.verticalLayout, 4, 0, 1, 3)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"Sitka Small")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setIndent(65)

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 3)

        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"MingLiU_HKSCS-ExtB")
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.label_3.setIndent(17)

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 3)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/font_awesome_regular/icons/font_awesome/regular/user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setMargin(8)
        self.label_4.setIndent(96)

        self.gridLayout_3.addWidget(self.label_4, 1, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(9)
        self.gridLayout_2.setVerticalSpacing(18)
        self.gridLayout_2.setContentsMargins(5, 3, 13, 6)
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 28))
        self.pushButton_2.setMaximumSize(QSize(16777215, 28))
        self.pushButton_2.setStyleSheet(u"            QPushButton {\n"
"                background-color: #ffffff;\n"
"                border: 1px solid #ffffff;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #ffffff;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #ffffff;\n"
"            }")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/login.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 5, 0, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(63, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(63, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setIndent(24)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 7, 0, 1, 3)

        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"            QPushButton {\n"
"                background-color: #ffffff;\n"
"                border: 1px solid #ffffff;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #ffffff;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #ffffff;\n"
"            }")

        self.gridLayout_3.addWidget(self.pushButton, 6, 0, 1, 3)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_5 = QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font)
        self.label_8.setIndent(59)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 3)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/font_awesome_regular/icons/font_awesome/regular/user.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setMargin(8)
        self.label_5.setIndent(96)

        self.gridLayout_5.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setIndent(30)

        self.gridLayout_5.addWidget(self.label_7, 8, 0, 1, 3)

        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setIndent(22)

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 3)

        self.horizontalSpacer_5 = QSpacerItem(63, 30, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(63, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(16, 9, 2, 3)
        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QSize(177, 30))
        self.lineEdit_3.setMaximumSize(QSize(177, 30))
        self.lineEdit_3.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #ffffff;\n"
"                padding: 6px;\n"
"                border-radius: 6px;\n"
"                background-color: #ffffff;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QSize(177, 30))
        self.lineEdit_4.setMaximumSize(QSize(177, 30))
        self.lineEdit_4.setStyleSheet(u"            QLineEdit {\n"
"                border: 1px solid #ffffff;\n"
"                padding: 6px;\n"
"                border-radius: 6px;\n"
"                background-color: #ffffff;\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"            }")
        self.lineEdit_4.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.checkBox = QCustomCheckBox(self.page_2)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.checkBox)


        self.gridLayout_5.addLayout(self.verticalLayout_2, 3, 0, 1, 3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(4)
        self.gridLayout_6.setVerticalSpacing(15)
        self.gridLayout_6.setContentsMargins(5, 7, 14, 6)
        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setStyleSheet(u"            QPushButton {\n"
"                background-color: #ffffff;\n"
"                border: 1px solid #ffffff;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 16px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #ffffff;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #ffffff;\n"
"            }")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/assignment_ind.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)

        self.gridLayout_6.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_6, 5, 0, 1, 3)

        self.pushButton_4 = QPushButton(self.page_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"            QPushButton {\n"
"                background-color: #ffffff;\n"
"                border: 1px solid #ffffff;\n"
"                border-radius: 13px;  /* Borda arredondada (c\u00edrculo) */\n"
"                color: black;  /* Cor do texto alterada para preto */\n"
"                font-size: 9px;  /* Ajuste do tamanho do \u00edcone */\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #ffffff;\n"
"            }\n"
"            QPushButton:pressed {\n"
"                background-color: #ffffff;\n"
"            }")

        self.gridLayout_5.addWidget(self.pushButton_4, 6, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_8.addWidget(self.stackedWidget, 1, 0, 1, 2)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User or Gmail..", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter your information bellow", None))
        self.label_4.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"@UrobotSoftware 2023 - 2024", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Not registered? Register", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"@UrobotSoftware 2023 - 2024", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Enter your information bellow", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User or Gmail..", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password...", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Agree with our terms", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Already registered? Login", None))
    # retranslateUi

