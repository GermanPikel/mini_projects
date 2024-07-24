from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(1200, 500, 500, 500)
        self.setWindowTitle('Перемешатор')
        self.init_ui()

    def init_ui(self):
        self.label1 = QLabel(self)
        self.label1.setText("my first label")
        self.label1.move(50, 50)
        self.b1 = QPushButton(self)
        self.b1.setText('Click me')
        self.b1.size()
        self.b1.move(100, 100)
        self.b1.clicked.connect(self.clicked_b1)

    def clicked_b1(self):
        self.label1.setText('You pressed the button')
        self.update()

    def update(self):
        self.label1.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()