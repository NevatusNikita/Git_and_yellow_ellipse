import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('01.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.draw)
        self.do_paint = False
        self.centre_x = 400
        self.centre_y = 300

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        fib_x = randint(1, 280)
        fib_y = randint(1, 280)
        circle_x1 = self.centre_x - fib_x
        circle_x2 = self.centre_x + fib_x
        circle_y1 = self.centre_y - fib_y
        circle_y2 = self.centre_y + fib_y
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(circle_x1, circle_y1, circle_x2, circle_y2)
        self.paint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
