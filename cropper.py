# Нужно сделать обработку в виде проекта(папки) processing с
# подкаталогами для шагов обработки
# 1) rotates
# 2) vertical_cut (к именам файлов добавим _vcN(0, 1, 2, ...))
# 3) horizontal_cut (к именам файлов добавим _hcN(0, 1, 2, ...))
# 4) orientation
# 5) angle_adjust
# 6) word_select (к именам файлов добавим _wsN(00, 01, 02, ...))
# 7) letter_select(к именам файлов добавим _lsN(00, 01, 02, ...))
# Нажатие на кнопку действия создаёт(перезаписывает) файл(ы) в папке следующего этапа.
# К следующему этапу можно перейти если обработаны или подтверждены файлы текущего этапа


import os
from os import listdir
from os.path import isfile, join
import sys
import qdarkstyle
import traceback
import os

from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QMenu, QGraphicsPixmapItem, \
    QGraphicsItem, QLabel, QGroupBox, QVBoxLayout, QFormLayout, QWidget, QGraphicsView, QGraphicsScene, \
    QGraphicsPixmapItem, QGraphicsLineItem
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.Qt import QClipboard
from PyQt5.QtCore import QModelIndex
import icons_rc
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFont, ImageDraw

from cropper_ui import Ui_MainWindow
from classes import *
from functions import *


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.mouse_press_pos = None
        self.setupUi(self)
        self.theme = 'Dark'
        self.work_dir = None
        self.source_dir = None
        self.files = []
        self.thumbnails = []
        self.labels = []
        self.current_image_index = None
        self.rotates = []
        self.v_cut_x = []
        self.lines = []
        self.current_line = None
        self.check_list = []
        self.buttons = [self.new_project_btn, self.open_btn, self.save_btn, self.check_all_btn,
                        self.rotate_clock_btn, self.rotate_counter_clock_btn,
                        self.zoom_out_btn, self.zoom_in_btn, self.add_vertical_cut_btn,
                        self.add_horizontal_cut_btn, self.delete_cut_btn, self.sciss_btn,
                        self.previous_btn, self.next_btn]
        self.theme_btn.clicked.connect(self.change_theme)
        self.open_btn.clicked.connect(self.open_folder)
        self.rotate_clock_btn.clicked.connect(self.rotate_right)
        self.rotate_counter_clock_btn.clicked.connect(self.rotate_left)
        self.save_btn.clicked.connect(self.save_project)
        self.check_all_btn.clicked.connect(self.check_all)
        self.next_btn.clicked.connect(self.next_step)
        self.add_vertical_cut_btn.clicked.connect(self.add_vertical)
        self.new_project_btn.clicked.connect(self.create_new_project)
        self.source_lb.setText('')
        self.source_lb.setGeometry(0, 0, 1000, 1000)
        self.source_lb.mousePressEvent = self.mousePressEvent
        self.v_cut = False
        self.h_cut = False
        self.image_viewer = None
        self.scene = None
        self.pixmap = None
        self.project = None
        self.show_buttons()

    def show_buttons(self):
        if self.project is None:
            button_state = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(len(self.buttons)):
                self.buttons[i].setVisible(button_state[i])
        elif self.project.current_step == 0:
            button_state = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
            for i in range(len(self.buttons)):
                self.buttons[i].setVisible(button_state[i])
        elif self.project.current_step == 1:
            button_state = [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1]
            for i in range(len(self.buttons)):
                self.buttons[i].setVisible(button_state[i])
            self.sciss_btn.setEnabled(False)

    def check_all(self):
        for check_box in self.check_list:
            check_box.setChecked(True)

    def vertical_cut(self):
        self.v_cut = True
        self.h_cut = False
        if self.image_viewer is not None:
            self.image_viewer.add_line(self.h_cut, self.h_cut)

    def add_vertical(self):
        self.v_cut = True
        self.h_cut = False
        if self.image_viewer is not None:
            if len(self.lines[self.current_image_index]) == 0:
                self.image_viewer.add_line(self.v_cut, self.h_cut)
                self.image_sa.show()
                self.sciss_btn.setEnabled(True)

    def horizontal_cut(self):
        self.h_cut = True
        self.v_cut = False

    def create_new_project(self):
        self.project = Project()
        if not self.project.new_project(self):
            return
        self.work_dir = self.project.work_dir + '/processing/' + self.project.steps[self.project.current_step]
        self.files = self.project.load_current_files()
        self.thumbnails = self.project.get_current_thumbnails()
        self.show_thumbnails()
        self.rotates = [0] * len(self.files)
        self.v_cut_x = [0] * len(self.files)
        self.setWindowTitle('Обработка изображений - выбор ориентации')
        self.show_buttons()

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

    def open_folder(self):
        temp_dir = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if temp_dir == '':
            return False
        self.project = Project(directory_name=temp_dir)
        if not self.project.load_project():
            return False
        self.files = self.project.load_current_files()
        self.thumbnails = self.project.get_current_thumbnails()
        checked = self.project.get_current_check_list()
        actions = self.project.get_current_action()
        if self.project.current_step == 0:
            self.rotates = actions
        self.show_thumbnails(checked)
        self.rotates = [0] * len(self.files)
        self.v_cut = None
        self.setWindowTitle('Обработка изображений - выбор ориентации')
        self.show_buttons()

    def show_thumbnails(self, checked=None):
        if checked is None:
            checked = []
        if len(self.thumbnails) > 0:
            v_layout = QVBoxLayout()
            group_box = QGroupBox()
            num = 1
            self.labels.clear()
            if self.project.current_step == 1:
                self.lines = [[] for _ in range(len(self.thumbnails))]
            for file in self.thumbnails:
                mini_v_layout = QVBoxLayout()
                label_num = QLabel(f'{num}:')
                check_box = QCheckBox()
                if len(checked) > num - 1:
                    check_box.setChecked(checked[num - 1])
                self.check_list.append(check_box)
                num += 1
                label = myLabel(self)
                label.setPixmap(QPixmap(file).scaled(200, 400, QtCore.Qt.KeepAspectRatio))
                self.labels.append(label)
                v_sp = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                mini_v_layout.addWidget(label_num)
                mini_v_layout.addWidget(check_box)
                mini_v_layout.addItem(v_sp)
                h_layout = QHBoxLayout()
                h_layout.addLayout(mini_v_layout)
                h_layout.addWidget(label)
                # v_layout.addRow(mini_v_layout, label)
                v_layout.addLayout(h_layout)
                if self.project.current_step == 0:
                    label.clicked.connect(self.thumbnail_click)
                elif self.project.current_step == 1:
                    label.clicked.connect(self.thumbnail_click_v_cut)
            group_box.setLayout(v_layout)
            self.thumbnails_sa.setWidget(group_box)
            self.thumbnails_sa.show()

    def thumbnail_click(self):
        for i in range(len(self.labels)):
            if self.labels[i] == self.sender():
                file = self.files[i]
                self.current_image_index = i
                self.image_viewer = ImageViewer(file)
                self.image_sa.setWidget(self.image_viewer)
                self.image_sa.show()

    def thumbnail_click_v_cut(self):
        for i in range(len(self.labels)):
            if self.labels[i] == self.sender():
                file = self.files[i]
                self.current_image_index = i
                self.image_viewer = ImageViewer(file, self.v_cut, self.h_cut)
                self.image_sa.setWidget(self.image_viewer)
                self.image_sa.show()

    def next_step(self):
        self.save_project()
        if self.project.next_step():
            self.work_dir = self.project.get_current_step_dir()
            self.thumbnails = []
            self.files = self.project.get_current_files()
            self.generate_thumbnails()
            self.show_thumbnails()
            self.setWindowTitle('Обработка изображений - ' + self.project.get_current_text_step())
            self.show_buttons()

    def rotate_right(self):
        self.rotates[self.current_image_index] += 90
        # self.rotates[self.current_image_index] %= 360
        if self.rotates[self.current_image_index] >= 0:
            self.write_on_thumbnails(f'Right {self.rotates[self.current_image_index]}')
        else:
            self.write_on_thumbnails(f'Left {-self.rotates[self.current_image_index]}')

    def rotate_left(self):
        self.rotates[self.current_image_index] -= 90
        # self.rotates[self.current_image_index] %= 360
        if self.rotates[self.current_image_index] >= 0:
            self.write_on_thumbnails(f'Right {self.rotates[self.current_image_index]}')
        else:
            self.write_on_thumbnails(f'Left {-self.rotates[self.current_image_index]}')

    def write_on_thumbnails(self, text):
        im = Image.open(self.thumbnails[self.current_image_index])
        font = ImageFont.truetype('./data/consolas.ttf', size=42)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (5, 5),
            text,
            font=font,
            fill=('#FF0000')
        )
        pix = pil2pixmap(im)
        self.labels[self.current_image_index].setPixmap(pix.scaled(200, 400, QtCore.Qt.KeepAspectRatio))

    def generate_thumbnails(self):
        self.thumbnails = []
        thumb_dir = self.work_dir + '/thumbnails'
        try:
            if not os.path.isdir(thumb_dir):
                os.mkdir(thumb_dir)
        except OSError:
            return False
        for file in self.files:
            image = Image.open(file)
            image.thumbnail((400, 400))
            new_name = self.work_dir + '/thumbnails/' + os.path.basename(file)
            image.save(new_name)
            self.thumbnails.append(new_name)

    def load_thumbnails(self):
        td = self.work_dir + '/thumbnails'
        self.thumbnails = [os.path.join(td, f) for f in os.listdir(td) if
                           os.path.isfile(os.path.join(td, f))]

    def rotate_image(self, angle):
        pass

    # https://python-scripts.com/draw-circle-rectangle-line

    def check_thumbnails(self):
        source = []
        thumbs = []
        for file in self.files:
            source.append(os.path.basename(file))
        for file in self.thumbnails:
            thumbs.append(os.path.basename(file))
        if source != thumbs:
            return False
        return True

    def open_image(self):
        # https://ru.stackoverflow.com/questions/1263508/Как-добавить-изображение-на-qgraphicsview
        fname, _ = QFileDialog.getOpenFileName(
            self, 'Open file', '.', 'Image Files (*.png *.jpg *.bmp)')
        if fname:
            pic = QGraphicsPixmapItem()
            pic.setPixmap(QPixmap(fname).scaled(160, 160))
            pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)

    def save_project(self):
        checked = []
        actions = []
        for cb in self.check_list:
            checked.append(cb.isChecked())
        if self.project.current_step == 0:
            actions = self.rotates
        self.project.set_current_action_steps(actions, checked)
        self.project.save_project()


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
