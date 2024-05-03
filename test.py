import sys
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QGraphicsLineItem
from PyQt5.QtCore import Qt, QPointF
from PyQt5.QtGui import QPixmap


class ImageViewer(QGraphicsView):
    def __init__(self, image_path):
        super().__init__()

        scene = QGraphicsScene(self)
        self.setScene(scene)

        pixmap = QGraphicsPixmapItem(QPixmap(image_path))
        scene.addItem(pixmap)

        self.line = QGraphicsLineItem(0, 0, 100, 0)
        self.line.setPen(Qt.red)
        scene.addItem(self.line)

        self.mouse_press_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mouse_press_pos is not None:
            delta = event.pos() - self.mouse_press_pos
            new_pos = self.line.pos() + delta
            self.line.setPos(new_pos)
            self.mouse_press_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_press_pos = None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    image_viewer = ImageViewer('image.jpg')
    image_viewer.show()

    sys.exit(app.exec_())
