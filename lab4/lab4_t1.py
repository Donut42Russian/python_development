import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5 import uic  # Импортируем uic


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI1.ui', self)  # Загружаем дизайн
        self.initUI()

    def initUI(self):
        self.new_img = 'new_color.jpg'
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        print(fname)
        self.pixmap = QPixmap(fname[0])
        self.pixmap_default = self.pixmap
        self.img_s = fname[0]
        self.label.setPixmap(self.pixmap)
        self.radioButton.clicked.connect(self.red)
        self.radioButton_2.clicked.connect(self.green)
        self.radioButton_3.clicked.connect(self.blue)
        self.radioButton_4.clicked.connect(self.default)

        self.angle = 0 #Параметр, необходимый для поворота
        self.Left.clicked.connect(self.keyPressEvent)
        self.Right.clicked.connect(self.keyPressEvent)

    def red(self):
        self.img = Image.open(self.img_s)
        self.pixels = self.img.load()
        x, y = self.img.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = r, 10, 10
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.label.setPixmap(self.pixmap)

        self.label.setPixmap(QPixmap(self.pixmap).transformed(QTransform().rotate(self.angle)))

    def green(self):
        self.img = Image.open(self.img_s)
        self.pixels = self.img.load()
        x, y = self.img.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 10, g, 10
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.label.setPixmap(self.pixmap)

        self.label.setPixmap(QPixmap(self.pixmap).transformed(QTransform().rotate(self.angle)))

    def blue(self):
        self.img = Image.open(self.img_s)
        self.pixels = self.img.load()
        x, y = self.img.size
        for i in range(x):
            for j in range(y):
                r, g, b = self.pixels[i, j]
                self.pixels[i, j] = 10, 10, b
        self.img.save(self.new_img)
        self.pixmap = QPixmap(self.new_img)
        self.label.setPixmap(self.pixmap)

        self.label.setPixmap(QPixmap(self.pixmap).transformed(QTransform().rotate(self.angle)))

    def default(self):
        self.pixmap = self.pixmap_default
        self.label.setPixmap(self.pixmap)

        self.label.setPixmap(QPixmap(self.pixmap).transformed(QTransform().rotate(self.angle)))

    def keyPressEvent(self, event):
        # on any key
        if self.sender() == self.Right:
            self.angle += 90
        elif self.sender() == self.Left:
            self.angle += -90
        t = QTransform().rotate(self.angle)
        self.label.setPixmap(QPixmap(self.pixmap).transformed(t))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setWindowTitle("1 задание")
    ex.show()
    sys.exit(app.exec_())
