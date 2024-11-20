import sqlite3
import sys

from PySide6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget, QMainWindow, QLabel
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex


class SimpleTableModel(QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        super().__init__(parent)
        self._data = data
        self._header = header

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._data)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._header)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header[section]
        return None


class TopUsers(QMainWindow):
    def __init__(self):
        super().__init__()
        f = open('user_name.txt', 'r')
        user = f.read()
        self.setWindowTitle("SQLite Table Viewer")
        conn = sqlite3.connect('users.sqlite')
        query = f"SELECT * FROM {user}"
        result = conn.execute(query)
        data = result.fetchall()
        header = [description[0] for description in result.description]
        conn.close()

        model = SimpleTableModel(data, header)
        view = QTableView()
        view.setModel(model)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(view)
        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 600, 600)
        self.attention = QLabel('ВНИМАНИЕ ТОП РАБОТАЕТ ТОЛЬКО ДЛЯ ТРЕКОВ ИЗ ПАПКИ')
        self.attention.setGeometry(300, 10, 100, 100)
