from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QSizePolicy
from login import Login
from register import Register


class Authorization(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/authorization.ui', self)
        self.login.clicked.connect(self.clicked_login)
        self.registor.clicked.connect(self.clicked_register)
        self.login_show = Login()
        self.register_show = Register()


    def clicked_login(self):
        self.hide()
        self.login_show.show()
        self.close()

    def clicked_register(self):
        self.hide()
        self.register_show.show()
        self.close()
