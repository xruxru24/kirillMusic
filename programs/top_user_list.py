import sqlite3
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, QTimer
from PySide6.QtWidgets import QMainWindow, QTableView, QVBoxLayout, QWidget


class SimpleTableModel(QAbstractTableModel):
    def __init__(self, data, header, parent=None):
        super().__init__(parent)
        self._data = data
        self._header = header

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._header)

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data[index.row()][index.column()])
        return None

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._header[section]
        return None


class TopUsers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таблица треков")
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_table)
        self.timer.start(3000)
        self.update_table()

    def update_table(self):
        f = open("user_name.txt", "r")
        table_name = f.read()
        conn = sqlite3.connect("users.sqlite")
        cursor = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        data = cursor.fetchall()
        header = [description[0] for description in cursor.description]
        conn.close()
        model = SimpleTableModel(data, header)
        view = self.findChild(QTableView)
        if view is None:
            view = QTableView()
            central_widget = QWidget()
            layout = QVBoxLayout(central_widget)
            layout.addWidget(view)
            self.setCentralWidget(central_widget)
        view.setModel(model)
