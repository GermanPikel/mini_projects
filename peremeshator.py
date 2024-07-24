import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from random import shuffle, randint
from pathlib import Path
import aspose.words as aw


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(220, 10, 311, 101))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.choose_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.choose_file_button.setGeometry(QtCore.QRect(290, 120, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_file_button.setFont(font)
        self.choose_file_button.setObjectName("choose_file_button")
        self.file_chosen = QtWidgets.QLabel(self.centralwidget)
        self.file_chosen.setGeometry(QtCore.QRect(150, 190, 461, 41))
        self.file_chosen.setAlignment(QtCore.Qt.AlignCenter)
        self.file_chosen.setObjectName("file_chosen")
        self.shuffle_button = QtWidgets.QPushButton(self.centralwidget)
        self.shuffle_button.setGeometry(QtCore.QRect(150, 280, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.shuffle_button.setFont(font)
        self.shuffle_button.setObjectName("shuffle_button")
        self.announcement_label = QtWidgets.QLabel(self.centralwidget)
        self.announcement_label.setGeometry(QtCore.QRect(170, 370, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.announcement_label.setFont(font)
        self.announcement_label.setText("")
        self.announcement_label.setAlignment(QtCore.Qt.AlignCenter)
        self.announcement_label.setObjectName("announcement_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Перемешатор"))
        self.main_label.setText(_translate("MainWindow", "ПЕРЕМЕШАТОР"))
        self.choose_file_button.setText(_translate("MainWindow", "Выбрать файл"))
        self.file_chosen.setText(_translate("MainWindow", "Файл не выбран."))
        self.shuffle_button.setText(_translate("MainWindow", "Перемешать и скачать перемешенный файл"))


def convert_to_txt(file):
    extension = os.path.splitext(file)[1]
    doc = aw.Document(file)
    doc.save("Output_converted.txt")
    with open("Output_converted.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i[:12] != "Created with" and i[:15] != "Evaluation Only":
                f.write(i)
        f.truncate()


def convert_to_word(id, extension):
    doc = aw.Document(f'output{id}.txt')
    doc.save(f"output{id}{extension}")


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.downloaded_file = ''
        self.status = 0
        self.id = 0
        self.extension = ''
        self.buttons()

    def buttons(self):
        self.choose_file_button.clicked.connect(self.choice_clicked)
        self.shuffle_button.clicked.connect(self.shuffle_file)

    def choice_clicked(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "Выберите файл",
                                                  "",
                                                  "Text files (*.txt *.doc *.docx)")
        if fileName:
            self.extension = os.path.splitext(fileName)[1]
            self.file_chosen.setText(fileName)
            self.downloaded_file = fileName

    def shuffle_file(self):
        if self.downloaded_file:

            self.id = randint(10000, 10000000000)

            if self.extension == '.txt':
                f1 = open(self.downloaded_file)
                words = [word for word in f1]
                f1.close()

                shuffle(words)
                print(words)

                file = open(f'output{self.id}.txt', 'a')
                file.close()

                f2 = open(f'output{self.id}.txt', mode='w')
                for w in words:
                    f2.write(w)
                f2.close()
            else:
                convert_to_txt(self.downloaded_file)
                f1 = open('Output_converted.txt')
                words = [word for word in f1]
                f1.close()

                shuffle(words)
                print(words)

                file = open(f'output{self.id}.txt', 'a')
                file.close()

                f2 = open(f'output{self.id}.txt', mode='w')
                for w in words:
                    f2.write(w)
                f2.close()
                convert_to_word(self.id, self.extension)
                os.remove(f'output{self.id}.txt')
                os.remove('Output_converted.txt')
            self.status = 1

        else:
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Для начала работы загрузите файл')
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()

        self.upload_file()
    def upload_file(self):
        if self.status:
            cur_path = os.path.abspath(os.getcwd())
            destination = str(Path.home() / "Downloads")
            src_path = os.path.join(cur_path, f'output{self.id}{self.extension}')
            dst_path = os.path.join(destination, f'output{self.id}{self.extension}')
            os.rename(src_path, dst_path)
            self.announcement_label.setText('Файл загружен в папку "Загрузки"')
            self.status = 0
            self.id = 0
            self.downloaded_file = ''
            self.extension = ''
            self.file_chosen.setText('Файл не выбран.')
        else:
            pass
            # msg = QMessageBox()
            # msg.setWindowTitle('Ошибка')
            # msg.setIcon(QMessageBox.Critical)
            # msg.setText('Прежде чем скачать файл, загрузите его и перемешайте.')
            # x = msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
