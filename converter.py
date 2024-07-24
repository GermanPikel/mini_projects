from multiprocessing import freeze_support
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

freeze_support()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 545)
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum G")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(160, 30, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum G")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.main_label.setFont(font)
        self.main_label.setAlignment(QtCore.Qt.AlignCenter)
        self.main_label.setObjectName("main_label")
        self.from_currency = QtWidgets.QComboBox(self.centralwidget)
        self.from_currency.setGeometry(QtCore.QRect(420, 120, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum G")
        font.setPointSize(12)
        self.from_currency.setFont(font)
        self.from_currency.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.from_currency.setObjectName("from_currency")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_currency.addItem("")
        self.from_label = QtWidgets.QLabel(self.centralwidget)
        self.from_label.setGeometry(QtCore.QRect(100, 120, 81, 61))
        self.from_label.setAlignment(QtCore.Qt.AlignCenter)
        self.from_label.setObjectName("from_label")
        self.from_amount = QtWidgets.QTextEdit(self.centralwidget)
        self.from_amount.setGeometry(QtCore.QRect(180, 120, 241, 61))
        self.from_amount.setObjectName("from_amount")
        self.to_currency = QtWidgets.QComboBox(self.centralwidget)
        self.to_currency.setGeometry(QtCore.QRect(180, 200, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Linux Biolinum G")
        font.setPointSize(12)
        self.to_currency.setFont(font)
        self.to_currency.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.to_currency.setObjectName("to_currency")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_currency.addItem("")
        self.to_label = QtWidgets.QLabel(self.centralwidget)
        self.to_label.setGeometry(QtCore.QRect(100, 200, 81, 61))
        self.to_label.setAlignment(QtCore.Qt.AlignCenter)
        self.to_label.setObjectName("to_label")
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(240, 280, 191, 61))
        self.convert_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.convert_button.setObjectName("convert_button")
        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(164, 355, 341, 61))
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setObjectName("result_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 47))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        self.actionHelp.setFont(font)
        self.actionHelp.setObjectName("actionHelp")
        self.menu.addAction(self.actionHelp)
        self.menubar.addAction(self.menu.menuAction())

        self.buttons()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Converter"))
        self.main_label.setText(_translate("MainWindow", "CURRENCY   CONVERTER"))
        self.from_currency.setItemText(0, _translate("MainWindow", "USD"))
        self.from_currency.setItemText(1, _translate("MainWindow", "RUB"))
        self.from_currency.setItemText(2, _translate("MainWindow", "EUR"))
        self.from_label.setText(_translate("MainWindow", "From"))
        self.to_currency.setItemText(0, _translate("MainWindow", "RUB"))
        self.to_currency.setItemText(1, _translate("MainWindow", "USD"))
        self.to_currency.setItemText(2, _translate("MainWindow", "EUR"))
        self.to_label.setText(_translate("MainWindow", "To"))
        self.convert_button.setText(_translate("MainWindow", "CONVERT"))
        self.result_label.setText(_translate("MainWindow", "Here will be your conversion!"))
        self.menu.setTitle(_translate("MainWindow", "Помощь"))
        self.actionHelp.setText(_translate("MainWindow", "Дробные числа"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))

    convertations = {'USD': {'RUB': 88.2824,
                             'EUR': 0.91747659,
                             'USD': 1},
                     'EUR': {'RUB': 96.2637,
                             'USD': 1.0899461,
                             'EUR': 1},
                     'RUB': {'EUR': 0.0102440,
                             'USD': 0.0111654,
                             'RUB': 1}}

    def buttons(self):
        self.convert_button.clicked.connect(self.make_convertion)
        self.actionHelp.triggered.connect(self.float_help)

    def make_convertion(self):
        amount = self.from_amount.toPlainText()
        from_currency = self.from_currency.currentText()
        to_currency = self.to_currency.currentText()
        if not amount.isdigit() and not all([n.isdigit() for n in amount.split('.')]):
            if ',' in amount:
                self.float_help()
            else:
                self.error()
        else:
            result = float(amount) * self.convertations[from_currency][to_currency]
            new_text = amount + '   ' + from_currency + '   is   ' + str("{:.2f}".format(result)) + '   ' + to_currency
            self.result_label.setText(new_text)

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle('Error')
        msg.setText('You can input only integer')
        msg.setIcon(QMessageBox.Critical)
        msg.setInformativeText('Try again')
        x = msg.exec_()

    def float_help(self):
        msg = QMessageBox()
        msg.setWindowTitle('Дробные числа')
        msg.setText('Для корректной работы вводите дробные числа со знаком "."')
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def update(self):
        self.result_label.adjustSize()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
