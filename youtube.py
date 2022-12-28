import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi
from pytube import YouTube

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()

        loadUi('youtube.ui', self)
        self.audio.clicked.connect(self.audio_self)
        self.video.clicked.connect(self.video_self)

    def audio_self(self):
        # try:
            url = str(self.input1.text())
            yt = YouTube(url)
            yt.streams.filter(only_audio = True).first().download("audio", f"{yt.title}.mp3")

            self.label.setText("Всё установилось!")


        # except:
        #     self.label.setText("Произошла ошибка, повторите загрузку!!!")

    def video_self(self):
        try:
            url = str(self.input1.text())

            yt = YouTube(url)
            yt.streams.filter(progressive=True, file_extension="mp4").first().download("video", f"{yt.title}.mp4")
            
            self.label.setText("Все установилось! ")

        except:
            self.label.setText("Произошла ошибка, повторите заного !!!")  

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
              
                