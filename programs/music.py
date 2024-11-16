import sys
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtWidgets import QApplication, QFileDialog
from PySide6.QtUiTools import loadUiType

Ui_MainWindow, QMainWindow = loadUiType('../ui/player.ui')


class MusicPlayer(QMainWindow, Ui_MainWindow):
    def __init__(self):
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

    def clicked_stop_play_button(self):
        if self.play_or_stop:
            self.player.pause()
            self.play_or_stop = False
            self.stop_play_button.setText('плей')
        else:
            self.player.play()
            self.play_or_stop = True
            self.stop_play_button.setText('стоп')

    def clicked_dialog_button(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Аудио файлы (*.mp3 *.wav *.ogg)")
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication([])
    sys.excepthook = except_hook
    main_window = MusicPlayer()
    main_window.show()
    sys.exit(app.exec())
