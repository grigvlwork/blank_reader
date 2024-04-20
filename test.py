from PyQt5.QtWidgets import QApplication, QLabel, QScrollArea, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap


class ImageScrollArea(QWidget):
    def __init__(self, image_path):
        super().__init__()

        self.setWindowTitle('Image Scroll Area')

        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)

        self.image_label = QLabel(self)
        self.image_label.setPixmap(QPixmap(image_path))

        self.scroll_area.setWidget(self.image_label)

        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll_area)


if __name__ == '__main__':
    app = QApplication([])

    image_path = 'image.jpg'
    window = ImageScrollArea(image_path)
    window.resize(640, 480)
    window.show()

    app.exec_()
