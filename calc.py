"""Калькулятор."""

# Чтобы запустилось приложение необходимо (В виртуальном окружении в этом нет 
# необходимости)!!!!!!!!!РЕШЕНИЕ: Найти папку где установлен python, перейти 
# по пути C:\Users\Андрей\AppData\Local\Programs\
# Python\Python38\Lib\site-packages\PyQt5\Qt\plugins
# найти тут папку platforms и перенести в папку где находится python
from PyQt5 import QtCore, QtGui, QtWidgets

_COLOR = "background-color: rgb(255, 170, 0);"
_HEIGHT = 51
_WIDTH = 61


class Ui_MainWindow(object):
    """Реализация калькулятора."""


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Калькулятор")
        MainWindow.resize(181, 374)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 181, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 85, 255); color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_COLOR)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 80, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(_COLOR)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 80, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(_COLOR)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 130, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(_COLOR)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 130, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(_COLOR)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(120, 130, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(_COLOR)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 180, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(_COLOR)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 180, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(_COLOR)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 180, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(_COLOR)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(0, 230, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet(_COLOR)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(60, 230, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet(_COLOR)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(120, 230, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(_COLOR)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(0, 280, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(_COLOR)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(60, 280, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(_COLOR)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(120, 280, _WIDTH, _HEIGHT))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(_COLOR)
        self.pushButton_15.setObjectName("pushButton_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 181, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()


    def retranslateUi(self, MainWindow):
        """Установка подписей."""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_10.setText(_translate("MainWindow", "0"))
        self.pushButton_11.setText(_translate("MainWindow", "+"))
        self.pushButton_12.setText(_translate(                                                                                                                                                                                                 "MainWindow", "-"))
        self.pushButton_13.setText(_translate("MainWindow", "*"))
        self.pushButton_14.setText(_translate("MainWindow", "/"))
        self.pushButton_15.setText(_translate("MainWindow", "="))


    def add_function(self):
        """Связывает нажатие на кнопку с функцией обработчиком."""
        self.pushButton.clicked.connect(lambda: self.write_number(self.pushButton.text()))
        self.pushButton_2.clicked.connect(lambda: self.write_number(self.pushButton_2.text()))
        self.pushButton_3.clicked.connect(lambda: self.write_number(self.pushButton_3.text()))
        self.pushButton_4.clicked.connect(lambda: self.write_number(self.pushButton_4.text()))
        self.pushButton_5.clicked.connect(lambda: self.write_number(self.pushButton_5.text()))
        self.pushButton_6.clicked.connect(lambda: self.write_number(self.pushButton_6.text()))
        self.pushButton_7.clicked.connect(lambda: self.write_number(self.pushButton_7.text()))
        self.pushButton_8.clicked.connect(lambda: self.write_number(self.pushButton_8.text()))
        self.pushButton_9.clicked.connect(lambda: self.write_number(self.pushButton_9.text()))
        self.pushButton_10.clicked.connect(lambda: self.write_number(self.pushButton_10.text()))
        self.pushButton_11.clicked.connect(lambda: self.write_number(self.pushButton_11.text()))
        self.pushButton_12.clicked.connect(lambda: self.write_number(self.pushButton_12.text()))
        self.pushButton_13.clicked.connect(lambda: self.write_number(self.pushButton_13.text()))
        self.pushButton_14.clicked.connect(lambda: self.write_number(self.pushButton_14.text()))
        self.pushButton_15.clicked.connect(self.results)


    def write_number(self, number):
        """Выводит на метку символы."""
        self.label.setText(self.label.text() + number)


    def results(self):
        """Решает выражение и выводит его."""
        res = eval(self.label.text())
        self.label.setText(str(res))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
