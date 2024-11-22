from PySide6.QtCore import Signal
from PySide6.QtUiTools import loadUiType
import sqlite3
from music import MusicPlayer

Ui_MainWindow, QMainWindow = loadUiType('../ui/register.ui')


class Register(Ui_MainWindow, QMainWindow):
    open = Signal()

    def __init__(self, auth_window):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.setupUi(self)
        self.back_button.clicked.connect(self.clicked_back_button)
        self.register_button.clicked.connect(self.clicked_register_button)
        self.auth_window = auth_window
        self.music_player_show = MusicPlayer()

        with open("../style/style_authorization.qss", "r") as f:
            self.setStyleSheet(f.read())

    def clicked_back_button(self):
        self.hide()
        self.auth_window.show()
        self.close()

    def clicked_register_button(self):
        if self.text_password.toPlainText() and self.text_password2.toPlainText() and self.text_login.toPlainText():
            if self.text_password.toPlainText() == self.text_password2.toPlainText():
                if self.text_login.toPlainText() == 'users':
                    self.error.setText('такой логин уже есть')
                else:
                    conn = sqlite3.connect("users.sqlite")
                    cursor = conn.cursor()
                    try:

                        cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)",
                                       (self.text_login.toPlainText(), self.text_password.toPlainText()))
                        self.error.setText('')
                        cursor.execute(f'''CREATE TABLE {self.text_login.toPlainText()} (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            track_name TEXT,
                            listening  INTEGER);''')
                        conn.commit()
                        conn.close()
                        f = open('user_name.txt', 'w')
                        f.write(self.text_login.toPlainText())
                        f.close()
                        self.hide()
                        self.music_player_show.show()
                        self.close()
                    except sqlite3.IntegrityError:
                        self.error.setText('такой логин уже есть')
                        conn.close()
                    except sqlite3.OperationalError:
                        self.error.setText('ошибка формата')
                        conn.close()
            else:
                self.error.setText("пароли не совпадают")
        else:
            self.error.setText("одна из строк пустая")
