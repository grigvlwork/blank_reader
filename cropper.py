import sys
import qdarkstyle

from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QMenu, QGraphicsPixmapItem, \
    QGraphicsItem
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.Qt import QClipboard
from PyQt5.QtCore import QModelIndex
import icons_rc
from PyQt5.QtGui import QPixmap

from cropper_ui import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.theme = 'Dark'
        self.theme_btn.clicked.connect(self.change_theme)
        self.open_btn.clicked.connect(self.open_image)

    def change_theme(self):
        if self.theme == 'Dark':
            icon = QtGui.QIcon("images/light.svg")
            self.theme = 'Light'
            self.theme_btn.setIcon(icon)
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.LightPalette))
        else:
            icon = QtGui.QIcon("images/night.svg")
            self.theme = 'Dark'
            self.theme_btn.setIcon(icon)
            app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette))

    def open_image(self):
        # https://ru.stackoverflow.com/questions/1263508/Как-добавить-изображение-на-qgraphicsview
        fname, _ = QFileDialog.getOpenFileName(
            self, 'Open file', '.', 'Image Files (*.png *.jpg *.bmp)')
        if fname:
            pic = QGraphicsPixmapItem()
            pic.setPixmap(QPixmap(fname).scaled(160, 160))
            pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
            pic.setOffset(12, 12)
            self.source_gv.scene.addItem(pic)


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
    ex = MyWidget()
    sys.excepthook = excepthook
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=qdarkstyle.DarkPalette))
    ex.show()
    sys.exit(app.exec_())
