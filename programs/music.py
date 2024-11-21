import sys
import os
from PySide6.QtCore import QUrl, QTimer, Qt, QAbstractListModel, QModelIndex, Signal
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QListView, QVBoxLayout, QFileDialog
from PySide6.QtUiTools import loadUiType
import sqlite3
from top_user_list import TopUsers

Ui_MainWindow, QMainWindow = loadUiType('../ui/player.ui')


class TrackModel(QAbstractListModel):
    def __init__(self, tracks, parent=None):
        super().__init__(parent)
        self._tracks = tracks

    def rowCount(self, index=QModelIndex()):
        return len(self._tracks)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._tracks[index.row()]
        return None


class MusicPlayer(QMainWindow, Ui_MainWindow):
    open = Signal()

    def __init__(self):
        self.top_users_list_show = TopUsers()
        super().__init__()
        self.setupUi(self)
        self.play_or_stop = True
        self.setWindowTitle("Музыкальный плеер")
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.file_name = None
        self.audio_output.setVolume(0.5)
        self.dialog_button.clicked.connect(self.clicked_dialog_button)
        self.volume_slider.setValue(50)
        self.volume_slider.setMaximum(100)
        self.volume_slider.setToolTip("Volume")
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.stop_play_button.clicked.connect(self.clicked_stop_play_button)
        self.progress_slider.setRange(0, 100)
        self.progress_slider.setValue(0)
        self.progress_slider.sliderMoved.connect(self.set_position)
        self.player.durationChanged.connect(self.set_duration)
        self.player.positionChanged.connect(self.set_position_value)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)
        self.timer.start(1000)
        self.append_playlist_button.clicked.connect(self.load_tracks_from_folder)
        self.top_user_button.clicked.connect(self.top_user_button_clicked)
        self.tracks = []
        self.track_list = QListView()
        self.track_list.clicked.connect(self.play_track_from_list)
        layout = QVBoxLayout(self.playlist_widget)
        layout.addWidget(self.track_list)
        self.playlist_widget.setVisible(False)
        self.listen_count = 0
        self.track_plays = {}
        self.half_duration = 0
        self.track_playing = False  # флаг для отслеживания воспроизведения

        with open("../style/style_authorization.qss", "r") as f:
            self.setStyleSheet(f.read())

    def top_user_button_clicked(self):
        self.top_users_list_show.show()

    def clicked_stop_play_button(self):
        if self.play_or_stop:
            self.player.pause()
            self.play_or_stop = False
            self.stop_play_button.setText('Воспроизвести')
        else:
            self.player.play()
            self.play_or_stop = True
            self.stop_play_button.setText('Пауза')

    def clicked_dialog_button(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Аудио файлы (*.mp3 *.wav *.ogg)")
        if self.file_name:
            self.player.setSource(QUrl.fromLocalFile(self.file_name))
            self.player.play()

    def set_volume(self):
        self.volume = self.volume_slider.value()
        self.audio_output.setVolume(self.volume * 0.01)

    def set_duration(self, duration):
        self.progress_slider.setMaximum(duration)

    def set_position(self, position):
        self.player.setPosition(position)

    def set_position_value(self, position):
        self.progress_slider.setValue(position)

    def update_position(self):
        self.progress_slider.setValue(self.player.position())

    def load_tracks_from_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Выберите папку с треками")
        if folder_path:
            self.tracks = []
            for filename in os.listdir(folder_path):
                if filename.endswith(('.mp3', '.wav', '.ogg')):
                    self.tracks.append(os.path.join(folder_path, filename))

            model = TrackModel(self.tracks)
            self.track_list.setModel(model)
            self.playlist_widget.setVisible(True)

    def play_track_from_list(self, index):
        self.current_index = index
        track_path = self.track_list.model()._tracks[index.row()]
        self.player.setSource(QUrl.fromLocalFile(track_path))
        self.player.play()
        self.player.durationChanged.connect(self.duration_changed)
        self.track_playing = False

    def duration_changed(self, duration):
        if duration > 0:
            self.half_duration = duration // 2
            self.player.positionChanged.connect(self.position_changed)

    def position_changed(self, position):
        if position >= self.half_duration and not self.track_playing:
            track_path = self.track_list.model()._tracks[self.current_index.row()]
            track_name = os.path.basename(track_path)
            self.track_played(track_name)
            self.track_playing = True

    def track_played(self, track_name):
        f = open('user_name.txt', 'r')
        user = f.read()
        f.close()
        conn = sqlite3.connect('users.sqlite')
        cur = conn.cursor()
        cur.execute(f"SELECT listening FROM {user} WHERE track_name = ?", (track_name,))
        row = cur.fetchone()
        if row:
            cur.execute(f"UPDATE {user} SET listening = listening + 1 WHERE track_name = ?", (track_name,))
        else:

            cur.execute(f"INSERT INTO {user} (track_name, listening) VALUES (?, 1)", (track_name,))
        conn.commit()
        conn.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
