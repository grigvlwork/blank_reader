from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import pickle
import os
import shutil


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


class Area:
    def __init__(self, points=None):
        if points is None:
            points = set()
        self.points = points

    def get_width(self):
        if len(self.points) == 0:
            return 0
        return max(p.x for p in self.points) - min(p.x for p in self.points)

    def get_height(self):
        if len(self.points) == 0:
            return 0
        return max(p.y for p in self.points) - min(p.y for p in self.points)

    def add_point(self, x, y):
        self.points.add(Point(x, y))

    def near(self, x, y):
        for p in self.points:
            if abs(p.x - x) == 1 or abs(p.y - y) == 1:
                return True
        return False


class myLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()


class Project:
    def __init__(self, directory_name=None, file_project_name=None):
        self.work_dir = directory_name
        self.file_project_name = file_project_name
        self.current_step = 0
        self.steps = ["rotates", "vertical_cut", "horizontal_cut", "angle_adjust", "word_select", "letter_select",
                      "output"]

    def __getstate__(self) -> dict:
        state = {}
        state["work_dir"] = self.work_dir
        state["file_project_name"] = self.file_project_name
        state["current_step"] = self.current_step
        return state

    def __setstate__(self, state: dict):
        self.work_dir = state["work_dir"]
        self.file_project_name = state["file_project_name"]
        self.current_step = state["current_step"]

    def load_project(self, file_name):
        try:
            with open(file_name, "rb") as fp:
                temp = pickle.load(fp)
                self.work_dir = temp.work_dir
                return True
        except OSError as e:
            print("OS error({0}): {1}".format(e.errno, e.strerror))
            return False

    def save_project(self):
        try:
            with open(self.file_project_name, "wb") as fp:
                pickle.dump(self, fp)
                return True
        except OSError as e:
            print("OS error({0}): {1}".format(e.errno, e.strerror))
            return False

    def new_project(self, window):
        self.work_dir = ""
        self.work_dir = QFileDialog.getExistingDirectory(window, 'Select Folder')
        if self.work_dir == "":
            return False
        if self.make_structure():
            self.file_project_name = self.work_dir + '/processing/' + os.path.basename(self.work_dir) + ".blr"
            self.save_project()
            return True
        else:
            return False

    def make_structure(self):
        try:
            if not os.path.isdir(self.work_dir + '/processing'):
                os.mkdir(self.work_dir + '/processing')
            for step in self.steps:
                if not os.path.isdir(self.work_dir + '/processing/' + step):
                    os.mkdir(self.work_dir + '/processing/' + step)
            files = os.listdir(self.work_dir)
            for fname in files:
                if os.path.isfile(os.path.join(self.work_dir, fname)):
                    shutil.copy2(os.path.join(self.work_dir, fname), self.work_dir + '/processing/rotates')
            return True
        except OSError:
            return False

    def next_step(self):
        if self.current_step < 6:
            self.current_step += 1
            return self.steps[self.current_step]
        else:
            return False


class ImageViewer(QGraphicsView):
    def __init__(self, image_path, v_cut=False, h_cut=False):
        super().__init__()
        self.v_cut = v_cut
        self.h_cut = h_cut
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.pixmap = QGraphicsPixmapItem(QPixmap(image_path).scaled(2000, 1000,
                                                                     aspectRatioMode=2))
        self.scene.addItem(self.pixmap)
        self.mouse_press_pos = None

    def add_line(self, v_cut=False, h_cut=False):
        self.v_cut = v_cut
        self.h_cut = h_cut
        if self.v_cut:
            self.line = QGraphicsLineItem(self.pixmap.pixmap().width() // 2, 0,
                                          self.pixmap.pixmap().width() // 2, self.pixmap.pixmap().height())
            self.line.setPen(Qt.red)
            self.scene.addItem(self.line)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and (self.v_cut or self.h_cut):
            self.mouse_press_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mouse_press_pos is not None and (self.v_cut or self.h_cut):
            delta = event.pos() - self.mouse_press_pos
            new_pos = self.line.pos() + delta
            self.line.setPos(new_pos)
            self.mouse_press_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and (self.v_cut or self.h_cut):
            self.mouse_press_pos = None
