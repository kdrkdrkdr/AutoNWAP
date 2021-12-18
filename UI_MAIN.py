# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI_MAIN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(771, 331)
        MainWindow.setMinimumSize(QSize(268, 167))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(380, 278, 371, 20))
        font = QFont()
        font.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)
        self.open_file_dir_btn = QPushButton(self.centralwidget)
        self.open_file_dir_btn.setObjectName(u"open_file_dir_btn")
        self.open_file_dir_btn.setGeometry(QRect(674, 54, 75, 23))
        self.log_browser = QTextBrowser(self.centralwidget)
        self.log_browser.setObjectName(u"log_browser")
        self.log_browser.setGeometry(QRect(19, 83, 731, 181))
        self.painted_file_dir = QLineEdit(self.centralwidget)
        self.painted_file_dir.setObjectName(u"painted_file_dir")
        self.painted_file_dir.setGeometry(QRect(20, 55, 551, 20))
        self.painted_file_dir.setReadOnly(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(15, 27, 481, 21))
        font1 = QFont()
        font1.setFamily(u"\ub9d1\uc740 \uace0\ub515")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_3.setFont(font1)
        self.select_file_dir_btn = QPushButton(self.centralwidget)
        self.select_file_dir_btn.setObjectName(u"select_file_dir_btn")
        self.select_file_dir_btn.setGeometry(QRect(588, 53, 75, 23))
        self.select_model_cbox = QComboBox(self.centralwidget)
        self.select_model_cbox.addItem("")
        self.select_model_cbox.addItem("")
        self.select_model_cbox.addItem("")
        self.select_model_cbox.addItem("")
        self.select_model_cbox.setObjectName(u"select_model_cbox")
        self.select_model_cbox.setGeometry(QRect(112, 276, 141, 22))
        self.run_paint_btn = QPushButton(self.centralwidget)
        self.run_paint_btn.setObjectName(u"run_paint_btn")
        self.run_paint_btn.setGeometry(QRect(268, 276, 91, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(15, 277, 91, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoNWAP \ub124\uc774\ubc84 \uc778\uacf5\uc9c0\ub2a5 \ucc44\uc0c9 \uc790\ub3d9\ud654 \ud504\ub85c\uadf8\ub7a8", None))
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.open_file_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc5f4\uae30", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\ucc44\uc0c9\ud560 \ud30c\uc77c\uc774 \uc788\ub294 \ud3f4\ub354 \uc704\uce58: <span style=\" color:#ff0000;\">\ucc44\uc0c9\ud560 \uc0ac\uc9c4\ub4e4\uc774 \uc788\ub294 \ud3f4\ub354\ub97c \uc120\ud0dd\ud558\uc138\uc694! </span></p></body></html>", None))
        self.select_file_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\ud3f4\ub354 \uc120\ud0dd", None))
        self.select_model_cbox.setItemText(0, QCoreApplication.translate("MainWindow", u"\uae30\ubcf8 \ubaa8\ub378", None))
        self.select_model_cbox.setItemText(1, QCoreApplication.translate("MainWindow", u"\ud3ec\uc2a4\ud130 \ubaa8\ub378", None))
        self.select_model_cbox.setItemText(2, QCoreApplication.translate("MainWindow", u"\uadf8\ub9ac\uc790\uc774\uc720 \ubaa8\ub378", None))
        self.select_model_cbox.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc804\uacbd \ub9c8\uc2a4\ud0b9", None))

        self.run_paint_btn.setText(QCoreApplication.translate("MainWindow", u"\ucc44\uc0c9 \uc2dc\uc791", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ucc44\uc0c9 \ubaa8\ub378 \uc120\ud0dd", None))
    # retranslateUi

