# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Il_Translit.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)
import icon_01_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 527)
        MainWindow.setStyleSheet(u"color: rgb(141, 195, 229);\n"
"border-color: rgb(85, 170, 255);\n"
"border-color: rgb(85, 170, 255);\n"
"font: 18pt \"Tahoma\";\n"
"color: rgb(230, 230, 115);\n"
"background-color: rgb(46, 57, 90);\n"
"font: 12pt \"Tahoma\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(141, 20, 69, 19))
        self.label.setStyleSheet(u"color: rgb(202, 202, 202);")
        self.translit_button = QPushButton(self.centralwidget)
        self.translit_button.setObjectName(u"translit_button")
        self.translit_button.setGeometry(QRect(141, 226, 431, 41))
        self.translit_button.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"\n"
"background-color: rgb(156, 104, 0);")
        icon = QIcon()
        icon.addFile(u":/icon_01/icons/post_add_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.translit_button.setIcon(icon)
        self.translit_button.setIconSize(QSize(24, 24))
        self.textBrowser_4 = QTextBrowser(self.centralwidget)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(20, 100, 90, 41))
        self.textBrowser_4.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_5 = QTextBrowser(self.centralwidget)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(20, 60, 90, 41))
        self.textBrowser_5.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_6 = QTextBrowser(self.centralwidget)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(20, 20, 90, 41))
        self.textBrowser_6.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_7 = QTextBrowser(self.centralwidget)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(20, 220, 90, 41))
        self.textBrowser_7.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_8 = QTextBrowser(self.centralwidget)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(20, 140, 90, 41))
        self.textBrowser_8.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_9 = QTextBrowser(self.centralwidget)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(20, 180, 90, 41))
        self.textBrowser_9.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_10 = QTextBrowser(self.centralwidget)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(20, 380, 90, 41))
        self.textBrowser_10.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_11 = QTextBrowser(self.centralwidget)
        self.textBrowser_11.setObjectName(u"textBrowser_11")
        self.textBrowser_11.setGeometry(QRect(20, 420, 90, 41))
        self.textBrowser_11.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_12 = QTextBrowser(self.centralwidget)
        self.textBrowser_12.setObjectName(u"textBrowser_12")
        self.textBrowser_12.setGeometry(QRect(20, 460, 90, 41))
        self.textBrowser_12.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_13 = QTextBrowser(self.centralwidget)
        self.textBrowser_13.setObjectName(u"textBrowser_13")
        self.textBrowser_13.setGeometry(QRect(20, 260, 90, 41))
        self.textBrowser_13.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.textBrowser_14 = QTextBrowser(self.centralwidget)
        self.textBrowser_14.setObjectName(u"textBrowser_14")
        self.textBrowser_14.setGeometry(QRect(20, 300, 90, 41))
        self.textBrowser_14.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(141, 298, 80, 19))
        self.label_2.setStyleSheet(u"color: rgb(202, 202, 202);")
        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(580, 226, 201, 41))
        self.clear_button.setStyleSheet(u"color: rgb(221, 221, 221);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon_01/icons/delete_white_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_button.setIcon(icon1)
        self.clear_button.setIconSize(QSize(24, 24))
        self.output_window = QLabel(self.centralwidget)
        self.output_window.setObjectName(u"output_window")
        self.output_window.setGeometry(QRect(140, 320, 641, 181))
        self.output_window.setStyleSheet(u"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.output_window.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.textBrowser_15 = QTextBrowser(self.centralwidget)
        self.textBrowser_15.setObjectName(u"textBrowser_15")
        self.textBrowser_15.setGeometry(QRect(20, 340, 90, 41))
        self.textBrowser_15.setStyleSheet(u"color: rgb(156, 104, 0);\n"
"font: 18pt \"Tahoma\";\n"
"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        self.input_window = QPlainTextEdit(self.centralwidget)
        self.input_window.setObjectName(u"input_window")
        self.input_window.setGeometry(QRect(140, 40, 640, 170))
        self.input_window.setStyleSheet(u"background-color: rgba(0, 0, 0, 35);\n"
"border: 1px solid rgb(156, 104, 0);\n"
"border-color: rgb(156, 104, 0);")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Translit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input text", None))
        self.translit_button.setText(QCoreApplication.translate("MainWindow", u"Translit and copy to clipboard      (Ctrl + T)", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u044b      y</p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0451    joo</p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0436    zh</p></body></html>", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0439       j</p></body></html>", None))
        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u044e     ju</p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u044f     ja</p></body></html>", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0447     ch</p></body></html>", None))
        self.textBrowser_11.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u044c       '</p></body></html>", None))
        self.textBrowser_12.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u044a      w</p></body></html>", None))
        self.textBrowser_13.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0448    sh</p></body></html>", None))
        self.textBrowser_14.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0449   sch</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output text", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Clear     (Ctrl + D)", None))
        self.output_window.setText("")
        self.textBrowser_15.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Tahoma'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0446     ts</p></body></html>", None))
    # retranslateUi

