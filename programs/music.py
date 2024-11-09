import sys

from PyQt6 import uic
from PyQt6.QtCore import, QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog


class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('../ui/player.ui', self)
        self.play_or_stop = True
        self.setWindowTitle("Музыкальный плеер")


    def clicked_spot_play_button(self):
        if self.play_or_stop:
            self.player.pause()
            self.play_or_stop = False
        else:
            self.player.play()
            self.play_or_stop = True

    def clicked_dialog_button(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Открыть файл", "", "Аудио файлы (*.mp3 *.wav *.ogg)")
        self.player.setSource(QUrl.fromLocalFile(self.file_name))
        self.player.play()

    def set_volume(self):
        self.volume = self.volume_slider.value()
        self.audio_output.setVolume(self.volume * .01)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication([])
    sys.excepthook = except_hook
    main_window = MusicPlayer()
    main_window.show()
    sys.exit(app.exec())