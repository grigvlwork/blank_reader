from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pickle


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
    def __init__(self, directory_name):
        self.work_dir = directory_name

    def __getstate__(self) -> dict:
        state = {}
        state["work_dir"] = self.work_dir
        return state

    def __setstate__(self, state: dict):
        self.work_dir = state["work_dir"]

    def load_project(self, file_name):
        try:
            with open(file_name, "rb") as fp:
                temp = pickle.load(fp)
                self.work_dir = temp.work_dir
                return True
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror)
            return False

    def save_project(self, file_name):
        try:
            with open(file_name, "wb") as fp:
                pickle.dump(self, fp)
                return True
        except IOError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror)
            return False
