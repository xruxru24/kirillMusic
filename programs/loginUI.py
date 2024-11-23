from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 533)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_authorization = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_authorization.setGeometry(QtCore.QRect(360, 20, 301, 141))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(False)
        font.setUnderline(False)
        self.label_authorization.setFont(font)
        self.label_authorization.setMouseTracking(False)
        self.label_authorization.setTabletTracking(False)
        self.label_authorization.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_authorization.setStyleSheet("")
        self.label_authorization.setObjectName("label_authorization")
        self.text_login = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_login.setGeometry(QtCore.QRect(260, 200, 301, 41))
        self.text_login.setObjectName("text_login")
        self.text_password = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.text_password.setGeometry(QtCore.QRect(260, 280, 301, 41))
        self.text_password.setObjectName("text_password")
        self.label_login = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(260, 170, 41, 21))
        self.label_login.setObjectName("label_login")
        self.label_password = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_password.setGeometry(QtCore.QRect(260, 250, 51, 16))
        self.label_password.setObjectName("label_password")
        self.login_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(260, 360, 121, 51))
        self.login_button.setStyleSheet("")
        self.login_button.setObjectName("login_button")
        self.back_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 131, 51))
        self.back_button.setStyleSheet("")
        self.back_button.setObjectName("back_button")
        self.error = QtWidgets.QLabel(parent=self.centralwidget)
        self.error.setGeometry(QtCore.QRect(250, 330, 301, 20))
        self.error.setStyleSheet("color: green;")
        self.error.setText("")
        self.error.setObjectName("error")
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
        self.label_authorization.setText(_translate("MainWindow", "ВХОД"))
        self.label_login.setText(_translate("MainWindow", "ЛОГИН"))
        self.label_password.setText(_translate("MainWindow", "ПАРОЛЬ"))
        self.login_button.setText(_translate("MainWindow", "Войти"))
        self.back_button.setText(_translate("MainWindow", "назад"))