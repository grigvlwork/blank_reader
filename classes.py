from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import pickle
import os
import shutil
from PIL import Image


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
        self.rotates = None
        self.steps = ["rotates", "vertical_cut", "horizontal_cut", "orientation", "angle_adjust", "word_select",
                      "letter_select", "output"]
        self.text_steps = ["выбор ориентации листа", "вертикальный разрез", "горизонтальный разрез",
                           "ориентация бланка", "подгонка угла поворота бланка", "выбор слов",
                           "выбор букв", "вывод результата"]
        if directory_name is not None:
            self.load_project()
        else:
            self.action_steps = [0 for i in range(7)]

    def __getstate__(self) -> dict:
        state = {}
        state["work_dir"] = self.work_dir
        state["file_project_name"] = self.file_project_name
        state["current_step"] = self.current_step
        state["rotates"] = self.rotates
        state["action_steps"] = self.action_steps
        return state

    def set_current_action_steps(self, action, check_list):
        files = self.load_current_files()
        self.action_steps[self.current_step] = list(zip(files, action, check_list))

    def get_current_files(self):
        files, _, __ = zip(*self.action_steps[self.current_step])
        return files

    def get_current_action(self):
        _, action, __ = zip(*self.action_steps[self.current_step])
        return action

    def get_current_text_step(self):
        return self.text_steps[self.current_step]

    def get_current_check_list(self):
        _, __, check_list = zip(*self.action_steps[self.current_step])
        return check_list

    def get_current_step_dir(self):
        return self.work_dir + '/processing/' + self.steps[self.current_step]

    def rotate(self, source, destination, angle):
        try:
            file = source
            new_file = destination
            im = Image.open(file)
            im_rotate = im.rotate(-angle, expand=True)
            im_rotate.save(new_file, quality=100)
            im.close()
            return True
        except OSError:
            return False

    def __setstate__(self, state: dict):
        self.work_dir = state["work_dir"]
        self.file_project_name = state["file_project_name"]
        self.current_step = state["current_step"]
        self.rotates = state["rotates"]
        self.action_steps = state["action_steps"]

    def load_project(self):
        file_name = self.get_possible_project_name()
        try:
            with open(file_name, "rb") as fp:
                temp = pickle.load(fp)
                self.work_dir = temp.work_dir
                self.file_project_name = temp.file_project_name
                self.current_step = temp.current_step
                self.rotates = temp.rotates
                self.action_steps = temp.action_steps
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

    def get_possible_project_name(self):
        return self.work_dir + '/processing/' + os.path.basename(self.work_dir) + ".blr"

    def set_action(self, current_action):
        self.action_steps[self.current_step] = current_action

    def new_project(self, window):
        self.work_dir = ""
        self.work_dir = QFileDialog.getExistingDirectory(window, 'Select Folder')
        # Проверить что в папке нет уже существующего проекта, если есть то либо загружаем старый либо создаем новый
        if self.work_dir == "":
            return False
        possible_project_name = self.get_possible_project_name()
        if os.path.isfile(possible_project_name):
            reply = QMessageBox.question(None, 'Проект существует',
                                         'В папке имеется проект, загрузить его?',
                                         QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.load_project()
                return True
        else:
            if self.make_structure():
                self.file_project_name = possible_project_name
                self.save_project()
                return True
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
        if self.current_step == 0:
            try:
                for filename in os.listdir(self.work_dir + '/processing/vertical_cut'):
                    file_path = os.path.join(self.work_dir + '/processing/vertical_cut', filename)
                    os.remove(file_path)
                if os.path.isdir(self.work_dir + '/processing/vertical_cut/thumbnails'):
                    shutil.rmtree(self.work_dir + '/processing/vertical_cut/thumbnails')
            except OSError:
                return False
            check_list = self.get_current_check_list()
            files = self.get_current_files()
            angles = self.get_current_action()
            t = 0
            for i in range(len(files)):
                if check_list[i]:
                    t += 1
                    if angles[i] != 0:
                        dest = self.work_dir + '/processing/vertical_cut/' + os.path.basename(files[i])
                        if not self.rotate(files[i], dest, angles[i]):
                            return -1
                    else:
                        shutil.copy2(files[i], self.work_dir + '/processing/vertical_cut')
            action = [0 for _ in range(t)]
            check_list = [False for _ in range(t)]
            self.current_step += 1
            self.set_current_action_steps(action, check_list)
            self.save_project()
            return self.current_step
        # if self.current_step < 7:
        #     self.current_step += 1
        #     return self.steps[self.current_step]
        # else:
        #     return False

    def load_current_files(self):
        if self.work_dir is None:
            return ''
        else:
            current_step_dir = self.work_dir + '/processing/' + self.steps[self.current_step]
            files = [os.path.join(current_step_dir, f) for f in os.listdir(current_step_dir) if
                     os.path.isfile(os.path.join(self.work_dir, f))]
            return files

    def generate_thumbnails(self):
        thumbnails = []
        for file in self.load_current_files():
            image = Image.open(file)
            image.thumbnail((400, 400))
            new_name = self.work_dir + '/processing/' + self.steps[self.current_step] + \
                       '/thumbnails/' + os.path.basename(file)
            image.save(new_name)
            thumbnails.append(new_name)
        return thumbnails

    def get_current_thumbnails(self):
        if os.path.isdir(self.work_dir + '/processing/' + self.steps[self.current_step] + '/thumbnails'):
            td = self.work_dir + '/processing/' + self.steps[self.current_step] + '/thumbnails'
            thumbnails = [os.path.join(td, f) for f in os.listdir(td) if
                          os.path.isfile(os.path.join(td, f))]
            return thumbnails
        else:
            os.mkdir(self.work_dir + '/processing/' + self.steps[self.current_step] + '/thumbnails')
            return self.generate_thumbnails()


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
        self.lines = []
        self.current_line = None

    def add_line(self, v_cut=False, h_cut=False):
        self.v_cut = v_cut
        self.h_cut = h_cut
        if self.v_cut:
            line = QGraphicsLineItem(self.pixmap.pixmap().width() // 2, 0,
                                     self.pixmap.pixmap().width() // 2, self.pixmap.pixmap().height())
            line.setPen(Qt.red)
            self.scene.addItem(line)
            self.lines.append(line)
            self.current_line = len(self.lines) - 1

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and (self.v_cut or self.h_cut):
            self.mouse_press_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mouse_press_pos is not None and (self.v_cut or self.h_cut):
            delta = event.pos() - self.mouse_press_pos
            new_pos = self.lines[self.current_line].pos() + delta
            self.lines[self.current_line].setPos(new_pos)
            self.mouse_press_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and (self.v_cut or self.h_cut):
            self.mouse_press_pos = None
