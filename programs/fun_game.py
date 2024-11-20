from PySide6.QtCore import QPointF, Qt, QRectF, QTimer
from PySide6.QtGui import QPainter, QColor, QPolygonF
from PySide6.QtWidgets import QWidget, QLabel
from random import randint


class FunGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)
        self.setFixedSize(600, 600)
        self.figures = []
        self.game_timer = QTimer()
        self.game_timer.timeout.connect(self.generate_figures)
        self.game_timer.start(3000)
        self.score = 0
        self.result = QLabel(str(self.score), self)
        self.result.setGeometry(1, 10, 1000, 1000)

        self.setStyleSheet("""
            QWidget {
                background-image: url(pudge.jpg); 
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
            }
        """)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(0, 0, 0))
        for figure in self.figures:
            self.draw_figure(qp, figure)
        qp.end()

    def draw_figure(self, qp, figure):
        rad = figure['rad']
        color = figure['color']
        qp.setBrush(color)
        if figure['type'] == 'круг':
            qp.drawEllipse(QPointF(*figure['center']), rad, rad)
        elif figure['type'] == 'квадрат':
            x, y = figure['center']
            delta = rad / 2
            qp.drawRect(QRectF(QPointF(x - delta, y - delta),
                               QPointF(x + delta, y + delta)))
        elif figure['type'] == 'треугольник':
            x, y = figure['center']
            delta = rad / 2
            top = QPointF(x, y - rad)
            left = QPointF(x - (rad ** 2 - (rad / 2) ** 2) ** 0.5, y + delta)
            right = QPointF(x + (rad ** 2 - (rad / 2) ** 2) ** 0.5, y + delta)
            qp.drawPolygon(QPolygonF((top, left, right)))

    def generate_figures(self):
        self.figures = []
        for _ in range(3):
            figure_type = ['круг', 'квадрат', 'треугольник'][randint(0, 2)]
            rad = randint(20, 80)
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            center_x = randint(rad, self.width() - rad)
            center_y = randint(rad, self.height() - rad)
            self.figures.append({
                'type': figure_type,
                'rad': rad,
                'color': color,
                'center': (center_x, center_y)
            })
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            for i in range(len(self.figures)):
                figure = self.figures[i]
                if figure['type'] == 'треугольник':
                    x, y = figure['center']
                    rad = figure['rad']
                    top = QPointF(x, y - rad)
                    left = QPointF(x - (rad ** 2 - (rad / 2) ** 2) ** 0.5, y + rad / 2)
                    right = QPointF(x + (rad ** 2 - (rad / 2) ** 2) ** 0.5, y + rad / 2)
                    triangle_polygon = QPolygonF([top, left, right])
                    if triangle_polygon.containsPoint(QPointF(event.pos()), Qt.FillRule.OddEvenFill):
                        self.figures.pop(i)
                        self.score += 1
                        self.result.setText(str(self.score))
                        self.update()
                        break
                else:
                    x, y = figure['center']
                    rad = figure['rad']
                    if (event.pos().x() - x) ** 2 + (event.pos().y() - y) ** 2 <= rad ** 2:
                        self.figures.pop(i)
                        self.score += 1
                        self.result.setText(str(self.score))
                        self.update()
                        break
