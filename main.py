from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys


class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()

        loadUi('calc.ui', self)
        self.add.clicked.connect(self.add_num)
        self.min.clicked.connect(self.min_num)
        self.mul.clicked.connect(self.mul_num)
        self.div.clicked.connect(self.div_num)

    def add_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.res.setText(str(num1 + num2))
        except:
            self.res.setText('Input numbers!')

    
    def min_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.res.setText(str(num1 - num2))
        except:
            self.res.setText('Input numbers!')



    def mul_num(self):
        try:
            num1 = int(self.input1.text())
            num2 = int(self.input2.text())
            self.res.setText(str(num1 * num2))
        except:
            self.res.setText('Input numbers!')

    
    def div_num(self):
        try:
            try:
                num1 = int(self.input1.text())
                num2 = int(self.input2.text())
                self.res.setText(str(num1 / num2))
            except:
                if num1 == 0 and num2 == 0:
                    self.res.setText('Dumb! Division by zero is not allowed!')
                else:
                    pass
        except:
            self.res.setText('Input numbers!')

    

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()