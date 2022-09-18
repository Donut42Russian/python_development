import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit, QCheckBox
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.button0 = QPushButton(self)
        self.button0.move(10, 10)
        self.button0.setText("Кнопка1")

        self.cb0 = QCheckBox('Скрыть кнопку', self)
        self.cb0.move(150, 10)
        self.cb0.toggle()
        self.cb0.stateChanged.connect(self.hideWidget)

        self.input1 = QLineEdit(self)
        self.input1.move(10, 40)
        self.input1.setText("Поле ввода")

        self.cb1 = QCheckBox('Скрыть поле ввода', self)
        self.cb1.move(150, 40)
        self.cb1.toggle()
        self.cb1.stateChanged.connect(self.hideWidget)

        self.button1 = QPushButton(self)
        self.button1.move(10, 70)
        self.button1.setText("Кнопка2")

        self.cb2 = QCheckBox('Скрыть кнопку', self)
        self.cb2.move(150, 70)
        self.cb2.toggle()
        self.cb2.stateChanged.connect(self.hideWidget)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Третье задание')
        self.show()


    def hideWidget(self, state):
        if self.sender() == self.cb0:
            if state != Qt.Checked:
                self.button0.hide()
            else:
                self.button0.show()
        elif self.sender() == self.cb1:
            if state != Qt.Checked:
                self.input1.hide()
            else:
                self.input1.show()
        elif self.sender() == self.cb2:
            if state != Qt.Checked:
                self.button1.hide()
            else:
                self.button1.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())