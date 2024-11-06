from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
import sqlite3


class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('register.ui', self)
        # вернуть потом
        self.register_button.clicked.connect(self.clicked_register_button)

    def clicked_back_button(self):
        from authorization import Authorization
        self.hide()
        style_auth_window = Authorization()
        style_auth_window.show()
        self.close()

    def clicked_register_button(self):
        if self.text_password.toPlainText() and self.text_password2.toPlainText() and self.text_login.toPlainText():
            if self.text_password.toPlainText() == self.text_password2.toPlainText():
                conn = sqlite3.connect("user.sqlite")
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)",
                               (self.text_login.toPlainText(), self.text_password.toPlainText()))
                conn.commit()
                conn.close()
            else:
                self.error.setText("пароли не совпадают")
        else:
            self.error.setText("одна из строк пустая")
