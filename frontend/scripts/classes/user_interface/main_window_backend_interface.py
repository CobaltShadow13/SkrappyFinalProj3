
from PySide6.QtWidgets import QMainWindow, QWidget, QPushButton
from frontend.scripts.classes.user_interface.main_window_class import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.pushButton = QPushButton(self)

