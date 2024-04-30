from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QLabel, QPushButton, QHBoxLayout,
                             QFileDialog, QMessageBox)
from PyQt5.QtGui import QImage, QMouseEvent, QTransform, QPixmap
from PyQt5.QtCore import Qt, QEvent
from PIL import Image, ImageQt
import sys
import traceback
import qdarkstyle
from PyQt5 import QtGui, QtCore


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
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.rotated_img = None
        self.image_label = QLabel(self)
        self.rotated_label = QLabel(self)
        self.load_btn = QPushButton("Load Image", self)
        self.load_btn.move(0, 500)
        self.save_btn = QPushButton("Save Rotated", self)
        self.save_btn.move(550, 500)
        self.mouse_down = None
        # horizontal_layout = QHBoxLayout()
        # horizontal_layout.addWidget(self.load_btn)
        # horizontal_layout.addWidget(self.save_btn)
        # self.image_label.setLayout(horizontal_layout)
        #
        self.load_btn.clicked.connect(self.load_image)
        self.save_btn.clicked.connect(self.save_rotated_image)

    def mousePressEvent(self, event: QMouseEvent):
        self.press_pos = event.pos()
        self.mouse_down = True

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.mouse_down = False

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if self.mouse_down:
            # Calculate angle of rotation
            angle = self.calculate_angle(event.pos(), self.press_pos)

            # Rotate PIL image
            self.rotated_img = self.apply_rotation(self.image, angle)

            # Update UI
            self.rotated_label.setPixmap(QPixmap(ImageQt(self.rotated_img)).scaledToWidth(300))

    def calculate_angle(self, pos, press_pos):
        # Calculate angle based on mouse delta
        return -(pos.x() - press_pos.x()) / (abs(pos.y() - press_pos.y()) + 1e-10)

    def apply_rotation(self, img, angle):
        # Rotate PIL image with the given angle
        rotated = img.rotate(angle)
        return rotated.resize(img.size, Image.BILINEAR)

    def save_rotated_image(self):
        # Get file path to save
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'Image Files (*.png *.jpg *.bmp)')

        if fileName:
            self.rotated_img.save(fileName, 'JPEG')
            print(f"Image saved to {fileName}")

    def load_image(self):
        fileName, _ = QFileDialog.getOpenFileName(self, 'Load Image', '', 'Image Files (*.png *.jpg *.bmp)')

        if fileName:
            self.image = Image.open(fileName)
            pix = pil2pixmap(self.image)
            self.image_label.setPixmap(pix.scaled(400, 400, QtCore.Qt.KeepAspectRatio))

    def closeEvent(self, event):
        # self.save_rotated_image()
        # super().closeEvent(event)
        pass


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(tb)
    msg = QMessageBox.critical(
        None,
        "Error catched!:",
        tb
    )
    QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.excepthook = excepthook
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette))
    ex.show()
    sys.exit(app.exec_())
