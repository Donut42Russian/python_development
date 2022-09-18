import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Второе задание')

        self.button = QPushButton(self)
        self.button.move(110, 40)
        self.button.setText("Вычислить")
        self.button.clicked.connect(self.run)

        self.input_1 = QLineEdit(self)
        self.input_1.move(10, 120)

        self.input_2 = QLineEdit(self)
        self.input_2.move(150, 120)

        self.show()

    def run(self):
        self.input_2.setText(str(eval(self.input_1.text())))
        self.input_1.setText("")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())