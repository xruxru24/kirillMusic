from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 570)
        MainWindow.setAccessibleDescription("")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 60, 391, 111))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.text_login = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_login.setGeometry(QtCore.QRect(240, 190, 311, 41))
        self.text_login.setObjectName("text_login")
        self.text_password = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_password.setGeometry(QtCore.QRect(240, 270, 311, 41))
        self.text_password.setObjectName("text_password")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 170, 47, 13))
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 240, 47, 16))
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 320, 121, 21))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.text_password2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_password2.setGeometry(QtCore.QRect(240, 350, 311, 41))
        self.text_password2.setObjectName("text_password2")
        self.register_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(240, 440, 261, 51))
        self.register_button.setStyleSheet("")
        self.register_button.setObjectName("register_button")
        self.error = QtWidgets.QLabel(parent=self.centralwidget)
        self.error.setGeometry(QtCore.QRect(230, 400, 311, 21))
        self.error.setStyleSheet("color: green;")
        self.error.setText("")
        self.error.setObjectName("error")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 151, 51))
        self.back_button.setStyleSheet("")
        self.back_button.setObjectName("back_button")
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
        self.label.setText(_translate("MainWindow", "РЕГИСТРАЦИЯ"))
        self.label_2.setText(_translate("MainWindow", "ЛОГИН"))
        self.label_3.setText(_translate("MainWindow", "ПАРОЛЬ"))
        self.label_4.setText(_translate("MainWindow", "ПОВТОРИТЕ ПАРОЛЬ"))
        self.register_button.setText(_translate("MainWindow", "ЗАРЕГИСТРИРОВАТЬСЯ"))
        self.back_button.setText(_translate("MainWindow", "НАЗАД"))