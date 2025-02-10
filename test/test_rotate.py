# from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QPushButton, QHBoxLayout,
#                              QFileDialog, QMessageBox)
# from PyQt5.QtGui import QImage, QMouseEvent, QTransform, QPixmap
# from PyQt5.QtCore import Qt, QEvent
# from PIL import Image, ImageQt
# import sys
# import traceback
# import qdarkstyle
# from PyQt5 import QtGui, QtCore
#
#
# def pil2pixmap(image):
#     if image.mode == "RGB":
#         r, g, b = image.split()
#         im = Image.merge("RGB", (b, g, r))
#     elif image.mode == "RGBA":
#         r, g, b, a = image.split()
#         im = Image.merge("RGBA", (b, g, r, a))
#     elif image.mode == "L":
#         im = image.convert("RGBA")
#     im2 = im.convert("RGBA")
#     data = im2.tobytes("raw", "RGBA")
#     qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
#     pixmap = QtGui.QPixmap.fromImage(qim)
#     return pixmap
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.rotated_img = None
#         self.image_label = QLabel(self)
#         self.rotated_label = QLabel(self)
#         self.load_btn = QPushButton("Load Image", self)
#         self.load_btn.move(0, 500)
#         self.save_btn = QPushButton("Save Rotated", self)
#         self.save_btn.move(550, 500)
#         self.mouse_down = None
#         # horizontal_layout = QHBoxLayout()
#         # horizontal_layout.addWidget(self.load_btn)
#         # horizontal_layout.addWidget(self.save_btn)
#         # self.image_label.setLayout(horizontal_layout)
#         #
#         self.load_btn.clicked.connect(self.load_image)
#         self.save_btn.clicked.connect(self.save_rotated_image)
#
#     def mousePressEvent(self, event: QMouseEvent):
#         self.press_pos = event.pos()
#         self.mouse_down = True
#
#     def mouseReleaseEvent(self, event: QMouseEvent):
#         self.mouse_down = False
#
#     def mouseMoveEvent(self, event: QMouseEvent) -> None:
#         if self.mouse_down:
#             # Calculate angle of rotation
#             angle = self.calculate_angle(event.pos(), self.press_pos)
#
#             # Rotate PIL image
#             self.rotated_img = self.apply_rotation(self.image, angle)
#
#             # Update UI
#             self.rotated_label.setPixmap(QPixmap(ImageQt(self.rotated_img)).scaledToWidth(300))
#
#     def calculate_angle(self, pos, press_pos):
#         # Calculate angle based on mouse delta
#         return -(pos.x() - press_pos.x()) / (abs(pos.y() - press_pos.y()) + 1e-10)
#
#     def apply_rotation(self, img, angle):
#         # Rotate PIL image with the given angle
#         rotated = img.rotate(angle)
#         return rotated.resize(img.size, Image.BILINEAR)
#
#     def save_rotated_image(self):
#         # Get file path to save
#         fileName, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Image Files (*.png *.jpg *.bmp)')
#
#         if fileName:
#             self.rotated_img.save(fileName, 'JPEG')
#             print(f"Image saved to {fileName}")
#
#     def load_image(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, 'Load Image', '', 'Image Files (*.png *.jpg *.bmp)')
#
#         if fileName:
#             self.image = Image.open(fileName)
#             pix = pil2pixmap(self.image)
#             self.image_label.setPixmap(pix.scaled(400, 400, QtCore.Qt.KeepAspectRatio))
#
#     def closeEvent(self, event):
#         # self.save_rotated_image()
#         # super().closeEvent(event)
#         pass
#
#
# def excepthook(exc_type, exc_value, exc_tb):
#     tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
#     print(tb)
#     msg = QMessageBox.critical(
#         None,
#         "Error catched!:",
#         tb
#     )
#     QApplication.quit()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Window()
#     sys.excepthook = excepthook
#     # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette))
#     ex.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt
# from PIL import Image
#
#
# class ImageRotateApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.image_path = None
#         self.angle = 0
#
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Image Rotation App')
#         layout = QVBoxLayout()
#
#         self.image_label = QLabel()
#         layout.addWidget(self.image_label)
#
#         open_button = QPushButton('Open Image')
#         open_button.clicked.connect(self.openImage)
#         layout.addWidget(open_button)
#
#         rotate_button = QPushButton('Rotate Image')
#         rotate_button.clicked.connect(self.rotateImage)
#         layout.addWidget(rotate_button)
#
#         save_button = QPushButton('Save Image')
#         save_button.clicked.connect(self.saveImage)
#         layout.addWidget(save_button)
#
#         self.setLayout(layout)
#
#     def openImage(self):
#         file_dialog = QFileDialog()
#         self.image_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '', 'Image files (*.jpg *.png)')
#
#         pixmap = QPixmap(self.image_path)
#         self.image_label.setPixmap(pixmap)
#         self.image_label.setAlignment(Qt.AlignCenter)
#
#     def rotateImage(self):
#         if self.image_path:
#             image = Image.open(self.image_path)
#             self.angle += 90
#             rotated_image = image.rotate(self.angle, expand=True)
#             rotated_image.show()
#
#     def saveImage(self):
#         if self.image_path:
#             image = Image.open(self.image_path)
#             image.save('rotated_image.jpg')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ImageRotateApp()
#     window.show()
#     sys.exit(app.exec_())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt, QPoint
from PIL import Image


def pil2pixmap(image):
    if image.mode == "RGB":
        r, g, b = image.split()
        im = Image.merge("RGB", (b, g, r))
    elif image.mode == "RGBA":
        r, g, b, a = image.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif image.mode == "L":
        im = image.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

# Вроде работает но непонятно как
class ImageRotateApp(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path = None
        self.angle = 0
        self.last_pos = QPoint()
        self.image = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Rotation App')
        layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setMouseTracking(True)
        self.image_label.mouseMoveEvent = self.mouseMoveEvent
        layout.addWidget(self.image_label)

        open_button = QPushButton('Open Image')
        open_button.clicked.connect(self.openImage)
        layout.addWidget(open_button)

        save_button = QPushButton('Save Image')
        save_button.clicked.connect(self.saveImage)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def openImage(self):
        file_dialog = QFileDialog()
        self.image_path, _ = file_dialog.getOpenFileName(self, 'Open Image', '', 'Image files (*.jpg *.png)')
        if self.image_path:
            self.image = Image.open(self.image_path)
            pixmap = QPixmap(self.image_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            dx = event.pos().x() - self.last_pos.x()
            # dy = event.pos().y() - self.last_pos.y()
            self.angle -= dx / 20
            if self.image_path:
                rotated_image = self.image.rotate(self.angle, expand=True)
                self.image_label.setPixmap(pil2pixmap(rotated_image))
                self.image_label.show()

        self.last_pos = event.pos()

    def saveImage(self):
        if self.image_path:
            rotated_image = self.image.rotate(self.angle, expand=True)
            rotated_image.save('rotated_image.jpg')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageRotateApp()
    window.show()
    sys.exit(app.exec_())


# Запускается, но не работает
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# from PyQt5.QtGui import QPixmap, QPainter, QTransform
# from PyQt5.QtCore import Qt
#
# class ImageRotator(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Image Rotator')
#         self.setGeometry(100, 100, 400, 400)
#
#         self.image_label = QLabel(self)
#         self.image_label.setGeometry(50, 50, 300, 300)
#
#         self.image = QPixmap('image.jpg')
#         self.angle = 0
#
#         self.show()
#
#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#
#         transform = QTransform()
#         transform.translate(self.width() / 2, self.height() / 2)
#         transform.rotate(self.angle)
#         transform.translate(-self.image.width() / 2, -self.image.height() / 2)
#
#         painter.setTransform(transform)
#         painter.drawPixmap(0, 0, self.image)
#
#     def mouseMoveEvent(self, event):
#         if event.buttons() == Qt.LeftButton:
#             diff = event.pos() - event.lastPos()
#             self.angle += diff.x()
#             self.update()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     rotator = ImageRotator()
#     sys.exit(app.exec_())


# Не запускается
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCore import Qt, QPointF
# from PyQt5.QtGui import QPixmap, QImage, QPainter, QTransform
# from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
#
# class ImageRotator(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.scene = QGraphicsScene()
#         self.view = QGraphicsView(self.scene)
#         self.setCentralWidget(self.view)
#
#         self.image = None
#         self.is_rotating = False
#         self.last_pos = None
#
#         self.view.setDragMode(QGraphicsView.ScrollHandDrag)
#         self.view.setRenderHint(QPainter.Antialiasing)
#         self.view.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
#         self.view.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
#         self.view.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
#
#         self.rotate_image(0)
#
#     def load_image(self, filepath):
#         if not filepath:
#             return
#
#         pixmap = QPixmap.load(filepath)
#         if pixmap.isNull():
#             return
#
#         self.image_item = QGraphicsPixmapItem(pixmap)
#         self.scene.clear()
#         self.scene.addItem(self.image_item)
#         self.scene.setSceneRect(self.image_item.boundingRect())
#
#         self.center_on_item(self.image_item)
#
#     def center_on_item(self, item):
#         rect = item.boundingRect()
#         center_pos = rect.center()
#         self.view.centerOn(center_pos)
#
#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.is_rotating = True
#             self.last_pos = event.pos()
#
#     def mouseMoveEvent(self, event):
#         if self.is_rotating:
#             delta = event.pos() - self.last_pos
#             angle = -delta.y() * 0.15
#             self.rotate_image(angle)
#             self.last_pos = event.pos()
#
#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.is_rotating = False
#             self.last_pos = None
#
#     def rotate_image(self, angle):
#         if self.image_item:
#             transform = QTransform()
#             transform.rotate(angle)
#             self.image_item.setTransform(transform)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ImageRotator()
#     window.show()
#
#     filepath = 'image.jpg'  # Replace with the path to your image
#     window.load_image(filepath)
#
#     sys.exit(app.exec_())
