from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
import sqlite3


class Login(QMainWindow):
    def __init__(self, auth_window):
        super().__init__()
        uic.loadUi('../ui/login.ui', self)
        self.back_button.clicked.connect(self.clicked_back_button)
        self.login_button.clicked.connect(self.clicked_login_button)
        self.auth_window = auth_window

        with open("../style/style_authorization.qss", "r") as f:
            self.setStyleSheet(f.read())


    def clicked_back_button(self):
        self.hide()
        self.auth_window.show()
        self.close()

    def clicked_login_button(self):
        if self.text_login.toPlainText() and self.text_password.toPlainText():
            conn = sqlite3.connect("user.sqlite")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?",
                           (self.text_login.toPlainText(), self.text_password.toPlainText()))
            result = cursor.fetchone()
            conn.close()
            if result:
                print(result)
            else:
                self.error.setText("неверный логин или пароль")
        else:
            self.error.setText("одна из строк пустая")
