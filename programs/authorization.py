from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from login import Login
from register import Register


class Authorization(QMainWindow):
    closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/authorization.ui', self)
        self.login.clicked.connect(self.clicked_login)
        self.registor.clicked.connect(self.clicked_register)
        self.login_show = Login(self)
        self.register_show = Register(self)

    def closeEvent(self, event):
        self.closed.emit()
        super().closeEvent(event)

    def clicked_login(self):
        self.hide()
        self.login_show.show()
        self.close()

    def clicked_register(self):
        self.hide()
        self.register_show.show()
        self.close()
