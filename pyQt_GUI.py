from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()  # the same as super().__init__ since python3
        self.setGeometry(550, 400, 700, 300)
        self.setWindowTitle("Neptun english program")
        self.initUI()

    def initUI(self):  # here we put what we want in our window
        self.label = QtWidgets.QLabel(self)  # by making self. we add attributes to our object
        self.label.setText('My first label!')  # so, therefore further we will be able to have access to them
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click me!')
        self.b1.clicked.connect(self.click_b1)  # don't put brackets () !!! this function should act on command

    def click_b1(self):  # changing the text that the label shows (showing the possibility to change attributes)
        self.label.setText('You pressed the button_1')
        self.update()

    def update(self):  # make sufficient length for a new label
        self.label.adjustSize()


def click_b1():
    print('click')


def window():
    app = QApplication(sys.argv)  # giving OS config setup
    win = MyWindow()  # making a window
    win.show()
    sys.exit(app.exec_())  # making clean exit after execution of the program


window()

