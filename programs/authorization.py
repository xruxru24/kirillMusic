from PySide6.QtCore import Signal
from PySide6.QtUiTools import loadUiType
from login import Login
from register import Register
from fun_game import FunGame

Ui_MainWindow, QMainWindow = loadUiType('../ui/authorization.ui')


class Authorization(QMainWindow, Ui_MainWindow):
    closed = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login.clicked.connect(self.clicked_login)
        self.registor.clicked.connect(self.clicked_register)
        self.fun_game_button.clicked.connect(self.clicked_fun_game_button)
        self.login_show = Login(self)
        self.register_show = Register(self)
        self.fun_game_show = FunGame()
        self.show()

        with open("../style/style_authorization.qss", "r") as f:
            self.setStyleSheet(f.read())

    def clicked_fun_game_button(self):
        self.fun_game_show.show()

    def close_event(self, event):
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