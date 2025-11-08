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
        MainWindow.resize(1080, 882)
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
        self.frame.setGeometry(QRect(180, 130, 331, 171))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
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
        self.board_piece_name_label.setGeometry(QRect(10, 0, 49, 16))
        self.board_piece_family_label = QLabel(self.frame)
        self.board_piece_family_label.setObjectName(u"board_piece_family_label")
        self.board_piece_family_label.setGeometry(QRect(200, 0, 41, 16))
        self.board_piece_image_path_input_2 = QTextEdit(self.frame)
        self.board_piece_image_path_input_2.setObjectName(u"board_piece_image_path_input_2")
        self.board_piece_image_path_input_2.setGeometry(QRect(10, 80, 161, 31))
        self.board_piece_image_path_input_2.setLineWidth(13)
        self.board_piece_image_path_label = QLabel(self.frame)
        self.board_piece_image_path_label.setObjectName(u"board_piece_image_path_label")
        self.board_piece_image_path_label.setGeometry(QRect(10, 60, 81, 16))
        self.board_piece_shape_label = QLabel(self.frame)
        self.board_piece_shape_label.setObjectName(u"board_piece_shape_label")
        self.board_piece_shape_label.setGeometry(QRect(190, 60, 71, 20))
        self.board_piece_shape_input = QTextEdit(self.frame)
        self.board_piece_shape_input.setObjectName(u"board_piece_shape_input")
        self.board_piece_shape_input.setGeometry(QRect(190, 80, 111, 31))
        self.board_piece_shape_input.setLineWidth(13)
        self.board_piece_table_widget = QTableWidget(self.centralwidget)
        if (self.board_piece_table_widget.columnCount() < 4):
            self.board_piece_table_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.board_piece_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.board_piece_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.board_piece_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.board_piece_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.board_piece_table_widget.setObjectName(u"board_piece_table_widget")
        self.board_piece_table_widget.setGeometry(QRect(550, 120, 411, 601))
        self.smbpm_label = QLabel(self.centralwidget)
        self.smbpm_label.setObjectName(u"smbpm_label")
        self.smbpm_label.setGeometry(QRect(280, 10, 511, 51))
        self.smbpm_label.setStyleSheet(u"font: 700 24pt \"Arial Rounded MT\";\n"
"text-decoration: underline;")
        self.cbp_label = QLabel(self.centralwidget)
        self.cbp_label.setObjectName(u"cbp_label")
        self.cbp_label.setGeometry(QRect(250, 70, 191, 51))
        self.cbp_label.setStyleSheet(u"font: 700 14pt \"Arial Rounded MT\";\n"
"text-decoration: underline;")
        self.cbpl_label = QLabel(self.centralwidget)
        self.cbpl_label.setObjectName(u"cbpl_label")
        self.cbpl_label.setGeometry(QRect(630, 80, 251, 51))
        self.cbpl_label.setStyleSheet(u"font: 700 14pt \"Arial Rounded MT\";\n"
"text-decoration: underline;")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(160, 310, 371, 351))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.board_piece_matrix_input = QTextEdit(self.frame_2)
        self.board_piece_matrix_input.setObjectName(u"board_piece_matrix_input")
        self.board_piece_matrix_input.setGeometry(QRect(10, 50, 351, 261))
        self.board_piece_matrix_input.setLineWidth(13)
        self.board_piece_shape_matrix_label = QLabel(self.frame_2)
        self.board_piece_shape_matrix_label.setObjectName(u"board_piece_shape_matrix_label")
        self.board_piece_shape_matrix_label.setGeometry(QRect(20, 20, 321, 20))
        self.create_board_piece_button = QPushButton(self.centralwidget)
        self.create_board_piece_button.setObjectName(u"create_board_piece_button")
        self.create_board_piece_button.setGeometry(QRect(300, 670, 111, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.board_piece_name_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Input Name</span></p></body></html>", None))
        self.apriltag_family_input_box.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.board_piece_name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.board_piece_family_label.setText(QCoreApplication.translate("MainWindow", u"Family", None))
        self.board_piece_image_path_input_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Image_Path</span></p></body></html>", None))
        self.board_piece_image_path_label.setText(QCoreApplication.translate("MainWindow", u"Image_Path:", None))
        self.board_piece_shape_label.setText(QCoreApplication.translate("MainWindow", u"Shape Name:r", None))
        self.board_piece_shape_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Input Shape Name</span></p></body></html>", None))
        ___qtablewidgetitem = self.board_piece_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.board_piece_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tag Family", None));
        ___qtablewidgetitem2 = self.board_piece_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tag #", None));
        ___qtablewidgetitem3 = self.board_piece_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Print?", None));
        self.smbpm_label.setText(QCoreApplication.translate("MainWindow", u"SkrapMap Board Piece Manager", None))
        self.cbp_label.setText(QCoreApplication.translate("MainWindow", u"Create Board Piece:", None))
        self.cbpl_label.setText(QCoreApplication.translate("MainWindow", u"Current Board Piece List:", None))
        self.board_piece_matrix_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-style:italic;\">[1,1,1],[1,1,1],[1,1,1]</span></p></body></html>", None))
        self.board_piece_shape_matrix_label.setText(QCoreApplication.translate("MainWindow", u"Shape Matrix: (3x3 L house example: [1,1,1],[1,1,1],[1,1,0])", None))
        self.create_board_piece_button.setText(QCoreApplication.translate("MainWindow", u"Create New Piece", None))
    # retranslateUi

