import sys 
from PyQt5.QtWidgets import  QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi
from pytube import YouTube

class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()

        loadUi("ska.ui", self)
        self.video.clicked.connect(self.video_self)
        self.audio.clicked.connect(self.audio_self)


    def video_self(self):
        try:
            url = str(self.url.text())

            yt = YouTube(url)
            yt.streams.filter(progressive=True, file_extension="mp4").first().download("video", f"{yt.title}.mp4")

            self.url.setText("Все установилось! ")

            self.prosent.setValue(100)



        except:
            self.url.setText("Произошла ошибка, повторите заного !!!")

    def audio_self(self):
        try:
            
           url = str(self.url.text())

           yt = YouTube(url)
           yt.streams.filter(only_audio=True).first().download("audio", f"{yt.title}.mp3")

           self.url.setText("Все установилось")

           self.prosent.setValue(100)
        except:
            self.url.setText("Произошла ошибка, повторите заного !!!")


app =  QApplication(sys.argv)
form = Form()
form.show()
app.exec_ ()       
