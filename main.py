from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys
from pytube import YouTube


class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()

        loadUi('ytdownload.ui', self)

        self.audio.clicked.connect(self.audio_download)
        self.video.clicked.connect(self.video_download)

    def audio_download(self):
        url = str(self.url1.text())
        yout = YouTube(url)
        yout.streams.filter(only_audio=True).first().download("audio", f"{yout.title}.mp3")
        self.maintitle.text("Скачано!")

    def video_download(self):
        url = str(self.url1.text())
        yout = YouTube(url)
        yout.streams.filter(progressive=True, file_extension="mp4").first().download("video", f"{yout.title}.mp4")
        self.maintitle.text("Скачано!")

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()