from PySide6.QtCore import Signal
from PySide6.QtUiTools import loadUiType
import sqlite3
from music import MusicPlayer

Ui_MainWindow, QMainWindow = loadUiType('../ui/login.ui')


class Login(Ui_MainWindow, QMainWindow):
    open = Signal()

    def __init__(self, auth_window):
        super().__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.clicked_back_button)
        self.login_button.clicked.connect(self.clicked_login_button)
        self.music_player_show = MusicPlayer()
        self.auth_window = auth_window

        with open("../style/style_authorization.qss", "r") as f:
            self.setStyleSheet(f.read())

    def clicked_back_button(self):
        self.hide()
        self.auth_window.show()
        self.close()

    def clicked_login_button(self):
        if self.text_login.toPlainText() and self.text_password.toPlainText():
            conn = sqlite3.connect("users.sqlite")
            cursor = conn.cursor()
            cursor.execute("SELECT *FROM users WHERE login = ? AND password = ?",
                           (self.text_login.toPlainText(), self.text_password.toPlainText()))
            result = cursor.fetchone()
            conn.close()
            if result:
                f = open('user_name.txt', 'w')
                f.write(self.text_login.toPlainText())
                f.close()
                self.hide()
                self.music_player_show.show()
                self.close()
            else:
                self.error.setText("неверный логин или пароль")
        else:
            self.error.setText("одна из строк пустая")
