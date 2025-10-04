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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():

            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1375, 893)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1080, 720))
        MainWindow.setMaximumSize(QSize(2064, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(940, 40, 331, 171))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.create_board_piece_button = QPushButton(self.frame)
        self.create_board_piece_button.setObjectName(u"create_board_piece_button")
        self.create_board_piece_button.setGeometry(QRect(190, 80, 111, 51))
        self.board_piece_name_input = QTextEdit(self.frame)
        self.board_piece_name_input.setObjectName(u"board_piece_name_input")
        self.board_piece_name_input.setGeometry(QRect(10, 20, 161, 31))
        self.board_piece_name_input.setLineWidth(13)
        self.apriltag_family_input_box = QComboBox(self.frame)
        self.apriltag_family_input_box.addItem("")
        self.apriltag_family_input_box.setObjectName(u"apriltag_family_input_box")
        self.apriltag_family_input_box.setGeometry(QRect(180, 20, 131, 31))
        self.board_piece_name_label = QLabel(self.frame)
        self.board_piece_name_label.setObjectName(u"board_piece_name_label")
        self.board_piece_name_label.setGeometry(QRect(60, 0, 49, 16))
        self.board_piece_name_label_2 = QLabel(self.frame)
        self.board_piece_name_label_2.setObjectName(u"board_piece_name_label_2")
        self.board_piece_name_label_2.setGeometry(QRect(200, 0, 41, 16))
        self.board_piece_shape_label = QLabel(self.frame)
        self.board_piece_shape_label.setObjectName(u"board_piece_shape_label")
        self.board_piece_shape_label.setGeometry(QRect(70, 60, 41, 16))
        self.board_piece_shape_input_box = QComboBox(self.frame)
        self.board_piece_shape_input_box.addItem("")
        self.board_piece_shape_input_box.setObjectName(u"board_piece_shape_input_box")
        self.board_piece_shape_input_box.setGeometry(QRect(10, 90, 161, 31))
        self.board_piece_table_widget = QTableWidget(self.centralwidget)
        if (self.board_piece_table_widget.columnCount() < 4):
            self.board_piece_table_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.board_piece_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.board_piece_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.board_piece_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentPrint))
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setIcon(icon);
        self.board_piece_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.board_piece_table_widget.setObjectName(u"board_piece_table_widget")
        self.board_piece_table_widget.setGeometry(QRect(940, 250, 331, 541))
        self.board_grid_table_widget = QTableWidget(self.centralwidget)
        self.board_grid_table_widget.setObjectName(u"board_grid_table_widget")
        self.board_grid_table_widget.setGeometry(QRect(30, 20, 861, 821))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.board_grid_table_widget.sizePolicy().hasHeightForWidth())
        self.board_grid_table_widget.setSizePolicy(sizePolicy1)
        self.board_grid_table_widget.horizontalHeader().setVisible(False)
        self.board_grid_table_widget.horizontalHeader().setHighlightSections(False)
        self.board_grid_table_widget.verticalHeader().setVisible(False)
        self.board_grid_table_widget.verticalHeader().setHighlightSections(False)
        self.board_grid_label = QLabel(self.centralwidget)
        self.board_grid_label.setObjectName(u"board_grid_label")
        self.board_grid_label.setGeometry(QRect(380, 0, 61, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1060, 220, 71, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1375, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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

        ___qtablewidgetitem = self.board_piece_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.board_piece_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tag Family", None));
        ___qtablewidgetitem2 = self.board_piece_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tag #", None));
        self.board_grid_label.setText(QCoreApplication.translate("MainWindow", u"Board Grid", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Board Pieces", None))
    # retranslateUi

