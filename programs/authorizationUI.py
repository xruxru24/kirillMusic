from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 430)
        MainWindow.setStyleSheet("color: green;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login.setGeometry(QtCore.QRect(120, 180, 120, 50))
        self.login.setStyleSheet("")
        self.login.setObjectName("login")
        self.registor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.registor.setGeometry(QtCore.QRect(450, 180, 180, 50))
        self.registor.setStyleSheet("")
        self.registor.setObjectName("registor")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 20, 510, 110))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.fun_game_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fun_game_button.setGeometry(QtCore.QRect(750, 360, 41, 31))
        self.fun_game_button.setObjectName("fun_game_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "ВХОД"))
        self.registor.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.label.setText(_translate("MainWindow", "ДОБРО ПОЖАЛОВАТЬ В SoundFLow"))
        self.fun_game_button.setText(_translate("MainWindow", "!"))
