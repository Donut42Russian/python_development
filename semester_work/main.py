import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QPainter
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QLabel, QPushButton, QWidget
import pandas as pd
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.Qt import QImage


class PasswordError(Exception):
    pass


class LoginError(Exception):
    pass


class not_found(LoginError):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


class CopyError(PasswordError):
    pass


class invalid_password(PasswordError):
    pass


strs = [
    'йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю', 'qwertyuiop', 'asdfghjkl',
    'zxcvbnm'
]
low = set(''.join(strs))
up = set(''.join(strs).upper())
num = set('1234567890')


def pass_is_valid(psw):
    for i in range(len(psw) - 2):
        psw_ = psw[i:i + 3].lower()
        for i in strs:
            if psw_ in i:
                return False
    return True


def passworld_check(t):
    print(t)
    if not len(t) > 8: raise LengthError("пароль слишком короткий")
    if not (set(t) & num): raise DigitError("в пароле нет числе")
    if not (set(t) & up): raise LetterError("в пароле нет загланыйх букв")
    if not (set(t) & low): raise LetterError("в пароле нет маленьких букв")
    if not pass_is_valid(t): raise SequenceError("пароль слишком простой")
    return True


class DraggableLabel(QLabel):
    def __init__(self,parent):
        super(QLabel,self).__init__(parent)
        self.show()

    def set_pic(self,image):
        self.setPixmap(QPixmap(image))    

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.LeftButton:
            return
        
        mimedata = QMimeData()
        drag = QDrag(self)
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())

        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos()- self.rect().topLeft())
        dropAction = drag.exec_(Qt.MoveAction)


class enter_window(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('enter.ui', self)
        self.error.setStyleSheet("color:Red;")
        self.enter_btn.clicked.connect(self.enter)
        self.registration_btn.clicked.connect(self.registration)
        self.reg = registration_window()
        self.m = main_window()

        self.connection = sqlite3.connect("password.sqlite")

    def enter(self):
        try:
            self.error.setText("")
            login = self.login.text()
            passwor = self.password.text()
            chec = "select * from users"
            chec = self.connection.cursor().execute(chec).fetchall()
            for i in chec:
                if login in i:
                    if passwor in i:
                        break
                    else:
                        raise invalid_password("неверный пароль")
                else:
                    raise not_found("логин не найден")
            self.close()
            self.m.show()
        except (PasswordError, LoginError) as e:
            self.error.setText(str(e))

    def registration(self):
        self.close()
        self.reg.show()


class registration_window(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('registration.ui', self)
        self.error.setStyleSheet("color:Red;")
        self.registration_btn.clicked.connect(self.registration)
        self.m = main_window()

        self.connection = sqlite3.connect("password.sqlite")

    def registration(self):
        try:
            chec_login = "select login from users"
            chec_login = self.connection.cursor().execute(
                chec_login).fetchall()
            my_login = self.login.text()
            for i in chec_login:
                if my_login in i: raise LoginError("этот логин уже занят")
            password = self.password.text()
            passworld_check(password)
            passord_re = self.password_re.text()
            if password != passord_re: raise CopyError("пароли не совпадают")
            self.error.setText("")
            reg = f'''insert into users (login , password)
                            values ('{my_login}' , '{password}')'''
            self.connection.cursor().execute(reg)
            self.connection.cursor().execute('commit')
            self.close()
            self.m.show()
        except (PasswordError, LoginError) as e:
            self.error.setText(str(e))


class main_window(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.image = DraggableLabel(self)
        self.btn_image.clicked.connect(self.set_frame)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.image.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()

    def set_frame(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        self.set_picture()

    def set_picture(self):
        self.img = Image.open(self.fname[0]).convert("RGB")
        qim = ImageQt(self.img)
        self.pixmap = QPixmap(QImage(qim))
        self.pixmap = self.pixmap.scaled(self.pixmap.width() // 15,
                                         self.pixmap.height() // 15)
        self.image.set_pic(QImage(qim))
        self.image.resize(self.pixmap.width(), self.pixmap.height())
        self.image.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = enter_window()
    ex.show()
    sys.exit(app.exec())