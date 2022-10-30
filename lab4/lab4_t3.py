import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QInputDialog
import random
n = 0



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global n
        n, ok_pressed = QInputDialog.getInt(
            self, "Флаг", "Введите количество цветов:", 10, 10, 10, 1)
        if ok_pressed:
            self.setGeometry(300, 300, 200, 250)
            self.setWindowTitle('Рисование')

    def paintEvent(self, event):
        global n
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        global n
        for i in range(n):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            qp.setBrush(QColor(r, g, b))
            qp.drawRect(30, 50+30*i, 120, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.setGeometry(400, 350, 400, 600)
    ex.setWindowTitle("3 задание")
    ex.show()
    sys.exit(app.exec())
