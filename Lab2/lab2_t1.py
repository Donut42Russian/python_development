import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
from PyQt5.QtCore import Qt

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.run)


        """self.button_group = QButtonGroup()
        self.button_group.addButton(self.radioButton)
        self.button_group.addButton(self.radioButton_2)
        self.button_group.addButton(self.radioButton_3)
        self.button_group.buttonClicked.connect(self.color)"""

        self.radioButton.clicked.connect(self.color)
        self.radioButton_2.clicked.connect(self.color)
        self.radioButton_3.clicked.connect(self.color)

        self.btn_color = "black"

    def run(self):
        if self.sender() == self.pushButton:
            if self.btn_color == "red":
                self.label_3.setStyleSheet('color: rgb(255, 0, 0);')
            elif self.btn_color == "black":
                self.label_3.setStyleSheet('color: rgb(0, 0, 0);')
            elif self.btn_color == "blue":
                self.label_3.setStyleSheet('color: rgb(0, 0, 255);')
        elif self.sender() == self.pushButton_2:
            if self.btn_color == "red":
                self.label_4.setStyleSheet('color: rgb(255, 0, 0);')
            elif self.btn_color == "black":
                self.label_4.setStyleSheet('color: rgb(0, 0, 0);')
            elif self.btn_color == "blue":
                self.label_4.setStyleSheet('color: rgb(0, 0, 255);')
        elif self.sender() == self.pushButton_3:
            if self.btn_color == "red":
                self.label_5.setStyleSheet('color: rgb(255, 0, 0);')
            elif self.btn_color == "black":
                self.label_5.setStyleSheet('color: rgb(0, 0, 0);')
            elif self.btn_color == "blue":
                self.label_5.setStyleSheet('color: rgb(0, 0, 255);')

    def color(self):
        if self.sender() == self.radioButton:
            self.btn_color = "black"
        elif self.sender() == self.radioButton_2:
            self.btn_color = "blue"
        elif self.sender() == self.radioButton_3:
            self.btn_color = "red"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())