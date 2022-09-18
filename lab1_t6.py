import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Close', 'Bck', '', 'Clear',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]

        self.buttons = []

        for position, name in zip(positions, names):

            if name == '':
                self.out = QLineEdit('')
                grid.addWidget(self.out, *position)
                continue
            elif name == '=':
                self.buttons.append(QPushButton(name, self))
                grid.addWidget(self.buttons[len(self.buttons) - 1], *position)
                self.buttons[len(self.buttons) - 1].clicked.connect(self.calculate)
                continue
            elif name == 'Clear':
                self.buttons.append(QPushButton(name, self))
                grid.addWidget(self.buttons[len(self.buttons) - 1], *position)
                self.buttons[len(self.buttons) - 1].clicked.connect(self.clear)
                continue
            elif name == 'Close' or name == 'Bck':
                self.buttons.append(QPushButton(name, self))
                grid.addWidget(self.buttons[len(self.buttons) - 1], *position)
                continue
            else:
                self.buttons.append(QPushButton(name, self))
                self.buttons[len(self.buttons) - 1].clicked.connect(self.input)
                grid.addWidget(self.buttons[len(self.buttons) - 1], *position)

        self.move(500, 300)
        self.setWindowTitle('Calculator')
        self.show()

    def input(self):
        self.out.setText(self.out.text() + self.sender().text())

    def clear(self):
        self.out.setText("")

    def calculate(self):
        try:
            self.out.setText(str(round(eval(self.out.text()), 6)))
        except:
            self.out.setText("Неправильный ввод")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
