from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pickle
import os


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

    def __getstate__(self) -> dict:
        state = {}
        state["work_dir"] = self.work_dir
        state["file_project_name"] = self.file_project_name
        return state

    def __setstate__(self, state: dict):
        self.work_dir = state["file_project_name"]

    def load_project(self, file_name):
        try:
            with open(file_name, "rb") as fp:
                temp = pickle.load(fp)
                self.work_dir = temp.work_dir
                return True
        except OSError as e:
            print("OS error({0}): {1}".format(e.errno, e.strerror))
            return False

    def save_project(self, file_name):
        try:
            with open(file_name, "wb") as fp:
                pickle.dump(self, fp)
                return True
        except OSError as e:
            print("OS error({0}): {1}".format(e.errno, e.strerror))
            return False

    def new_project(self):
        self.work_dir = QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.file_project_name = os.path.basename(self.work_dir)
        print(self.file_project_name)

    def make_structure(self):
        if not os.path.isdir(self.source_dir + '/processing'):
            os.mkdir(self.source_dir + '/processing')
        if not os.path.isdir(self.source_dir + '/processing/rotates'):
            os.mkdir(self.source_dir + '/processing/rotates')
        if not os.path.isdir(self.source_dir + '/processing/v_cut'):
            os.mkdir(self.source_dir + '/processing/v_cut')
        if not os.path.isdir(self.source_dir + '/processing/h_cut'):
            os.mkdir(self.source_dir + '/processing/h_cut')
        if not os.path.isdir(self.source_dir + '/processing/angle_adjust'):
            os.mkdir(self.source_dir + '/processing/angle_adjust')
        if not os.path.isdir(self.source_dir + '/processing/word_select'):
            os.mkdir(self.source_dir + '/processing/word_select')
        if not os.path.isdir(self.source_dir + '/processing/letter_select'):
            os.mkdir(self.source_dir + '/processing/letter_select')









