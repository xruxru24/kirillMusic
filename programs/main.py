import sys
from PyQt6.QtWidgets import QApplication
from authorization import Authorization


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    main_window = Authorization()
    main_window.show()
    sys.exit(app.exec())
