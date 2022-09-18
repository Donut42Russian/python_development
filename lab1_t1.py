import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Первое задание')

        self.button = QPushButton(self)
        self.button.move(110, 40)
        self.button.setText("--->")
        self.button.clicked.connect(self.run)

        self.input_1 = QLineEdit(self)
        self.input_1.move(10, 120)

        self.input_2 = QLineEdit(self)
        self.input_2.move(150, 120)

        self.show()

    def run(self):
        if self.input_1.text() != "":
            self.input_2.setText(self.input_1.text())
            self.input_1.setText("")
            self.button.setText("<---")
        else:
            self.input_1.setText(self.input_2.text())
            self.input_2.setText("")
            self.button.setText("--->")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())