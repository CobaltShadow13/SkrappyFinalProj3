# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_class.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 598)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 120, 79, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 30, 49, 16))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(450, 10, 351, 161))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.create_board_piece_button = QPushButton(self.frame)
        self.create_board_piece_button.setObjectName(u"create_board_piece_button")
        self.create_board_piece_button.setGeometry(QRect(210, 73, 111, 51))
        self.board_piece_name_input = QTextEdit(self.frame)
        self.board_piece_name_input.setObjectName(u"board_piece_name_input")
        self.board_piece_name_input.setGeometry(QRect(10, 20, 161, 31))
        self.board_piece_name_input.setLineWidth(13)
        self.apriltag_family_input_box = QComboBox(self.frame)
        self.apriltag_family_input_box.setObjectName(u"apriltag_family_input_box")
        self.apriltag_family_input_box.setGeometry(QRect(200, 20, 131, 31))
        self.board_piece_name_label = QLabel(self.frame)
        self.board_piece_name_label.setObjectName(u"board_piece_name_label")
        self.board_piece_name_label.setGeometry(QRect(70, 0, 49, 16))
        self.board_piece_name_label_2 = QLabel(self.frame)
        self.board_piece_name_label_2.setObjectName(u"board_piece_name_label_2")
        self.board_piece_name_label_2.setGeometry(QRect(240, 0, 41, 16))
        self.board_piece_shape_label = QLabel(self.frame)
        self.board_piece_shape_label.setObjectName(u"board_piece_shape_label")
        self.board_piece_shape_label.setGeometry(QRect(70, 80, 41, 16))
        self.board_piece_shape_input_box = QComboBox(self.frame)
        self.board_piece_shape_input_box.addItem("")
        self.board_piece_shape_input_box.setObjectName(u"board_piece_shape_input_box")
        self.board_piece_shape_input_box.setGeometry(QRect(10, 100, 161, 31))
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(460, 190, 331, 351))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TestButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TestLabel", None))
        self.create_board_piece_button.setText(QCoreApplication.translate("MainWindow", u"Create New Piece", None))
        self.board_piece_name_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Input Name</span></p></body></html>", None))
        self.apriltag_family_input_box.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.board_piece_name_label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.board_piece_name_label_2.setText(QCoreApplication.translate("MainWindow", u"Family", None))
        self.board_piece_shape_label.setText(QCoreApplication.translate("MainWindow", u"Shape", None))
        self.board_piece_shape_input_box.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))


        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

