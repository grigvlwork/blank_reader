from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import pickle
import os
import shutil
from PIL import Image
from typing import Callable, NamedTuple, Union

STEPS = ["vertical_cut", "horizontal_cut", "orientation", "angle_adjust", "word_select",
         "letter_select", "output"]
TEXT_STEPS = ["вертикальный разрез", "горизонтальный разрез",
              "ориентация бланка", "подгонка угла поворота бланка", "выбор слов",
              "выбор букв", "вывод результата"]


class Action(NamedTuple):
    type: str  # "cut", "crop", "rotate"
    value: Union[int, tuple]  # Число или кортеж
    final: bool


class Mylabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()


class Project:
    def __init__(self, directory_name=None, file_project_name=None):
        self.work_dir = directory_name
        self.file_project_name = file_project_name
        self.current_step = 0
        self.files = None
        self.check_list = None
        self.steps = STEPS
        self.text_steps = TEXT_STEPS
        if directory_name is not None:
            self.load_project()
        else:
            self.actions = dict()  # {индекс_изображения: действие}

    def add_action_to_image(self, image_index, action: Action):
        self.actions[image_index] = action

    def create_viewer(self, path, image_index):
        if image_index in self.actions.keys():
            return ImageViewer(path, image_index, self.add_action_to_image,
                               self.current_step, current_action=self.actions[image_index])
        return ImageViewer(path, image_index, self.add_action_to_image, self.current_step)

    def __getstate__(self) -> dict:
        state = dict()
        state["work_dir"] = self.work_dir
        state["file_project_name"] = self.file_project_name
        state["current_step"] = self.current_step
        state["files"] = self.files
        state["actions"] = self.actions
        state["check_list"] = self.check_list
        return state

    def get_current_files(self):
        # files, _, __ = zip(*self.action_steps[self.current_step])
        return self.files

    def get_current_action(self):
        # _, action, __ = zip(*self.action_steps[self.current_step])
        return self.actions

    def get_current_text_step(self):
        return self.text_steps[self.current_step]

    def get_current_check_list(self):
        # _, __, check_list = zip(*self.action_steps[self.current_step])
        return self.check_list

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
        self.actions = state["actions"]
        self.files = state["files"]
        self.check_list = state["check_list"]

    def load_project(self):
        file_name = self.get_possible_project_name()
        try:
            with open(file_name, "rb") as fp:
                temp = pickle.load(fp)
                self.work_dir = temp.work_dir
                self.file_project_name = temp.file_project_name
                self.current_step = temp.current_step
                self.actions = temp.actions
                self.files = temp.files
                self.check_list = temp.check_list
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
                self.current_step = 0
                self.load_current_files()
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
                    shutil.copy2(os.path.join(self.work_dir, fname), self.work_dir + '/processing/vertical_cut')
            return True
        except OSError:
            return False

    def next_step(self):
        if self.current_step == 0:  # Переделать на вертикальный разрез
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
            self.actions = dict()
            self.check_list = [False for _ in range(t)]
            self.current_step += 1
            self.save_project()
            return self.current_step

    def load_current_files(self):
        if self.work_dir is None:
            return ''
        else:
            current_step_dir = self.work_dir + '/processing/' + self.steps[self.current_step]
            files = [os.path.join(current_step_dir, f) for f in os.listdir(current_step_dir) if
                     os.path.isfile(os.path.join(self.work_dir, f))]
            self.files = files
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
    def __init__(self, image_path, image_index,
                 on_action_added: Callable[[int, str], None],
                 current_step, current_action=None):
        super().__init__()
        self.current_step = current_step
        self.image_index = image_index
        self.on_action_added = on_action_added
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.pixmap = QPixmap(image_path)
        original_width = self.pixmap.width()
        original_height = self.pixmap.height()
        # Масштабирование изображения
        scaled_pixmap = self.pixmap.scaled(2000, 1000, transformMode=Qt.SmoothTransformation,
                                           aspectRatioMode=2)
        self.pixmap_item = QGraphicsPixmapItem(scaled_pixmap)
        self.scene.addItem(self.pixmap_item)
        self.scale_x = original_width / scaled_pixmap.width()
        self.scale_y = original_height / scaled_pixmap.height()
        self.mouse_press_pos = None
        self.line = None
        self.current_action = current_action
        if current_action is not None:
            self.apply_action()
        else:
            self.current_line = None

    def apply_action(self):
        if self.current_action.final:
            color = Qt.green
        else:
            color = Qt.red
        if self.current_action.type == 'vertical_cut':
            x = self.current_action.value / self.scale_x
            self.line = QGraphicsLineItem(x, 0, x, self.pixmap_item.pixmap().height())
            self.line.setPen(color)
            self.scene.addItem(self.line)

    def add_vertical_cut(self, position: int):
        action = Action(type="vertical_cut", value=position, final=False)
        self.on_action_added(self.image_index, action)

    def add_horizontal_cut(self, position: int):
        action = Action(type="horizontal_cut", value=position, final=False)
        self.on_action_added(self.image_index, action)

    def add_action(self, action):
        # self.actions.append(action)
        if self.on_action_added:
            self.on_action_added(self.image_index, action)  # Сообщаем Project

    def set_current_step(self, current_step):
        self.current_step = current_step

    def remove_line(self):
        if self.line is not None:
            self.scene.removeItem(self.line)
            self.line = None
            self.actions().remove(self.image_index)

    def add_line(self):
        if self.line is not None:
            return
        if self.current_step == 0:  # Вертикальный разрез
            self.line = QGraphicsLineItem(self.pixmap_item.pixmap().width() // 2, 0,
                                          self.pixmap_item.pixmap().width() // 2, self.pixmap_item.pixmap().height())
            self.line.setPen(Qt.red)
            self.scene.addItem(self.line)
            pos_in_original_image = QPointF(
                self.pixmap_item.pixmap().width() // 2 * self.scale_x,
                0
            )
            self.current_action = Action(type='vertical_cut', value=int(pos_in_original_image.x()), final=False)
            self.add_action(self.current_action)
        elif self.current_step == 1:  # Горизонтальный разрез
            # action = Action(type='horizontal_cut', value=int(pos_in_original_image.y()))
            pass

    def add_final_line(self):
        if self.line is not None:
            self.scene.removeItem(self.line)
            if self.current_action.type == 'vertical_cut':
                x = self.current_action.value / self.scale_x
                self.line = QGraphicsLineItem(x, 0, x, self.pixmap_item.pixmap().height())
                self.line.setPen(Qt.green)
                self.scene.addItem(self.line)
        # if self.current_step == 0:  # Вертикальный разрез
        #     self.line = QGraphicsLineItem(self.pixmap_item.pixmap().width() // 2, 0,
        #                                   self.pixmap_item.pixmap().width() // 2, self.pixmap_item.pixmap().height())
        #     self.line.setPen(Qt.red)
        #     self.scene.addItem(self.line)
        #     pos_in_original_image = QPointF(
        #         self.pixmap_item.pixmap().width() // 2 * self.scale_x,
        #         0
        #     )
        #     action = Action(type='vertical_cut', value=int(pos_in_original_image.x()), final=False)
        #     self.add_action(action)
        # elif self.current_step == 1:  # Горизонтальный разрез
        #     # action = Action(type='horizontal_cut', value=int(pos_in_original_image.y()))
        #     pass

    # def get_lines(self):
    #     return self.lines

    def get_index(self):
        return self.image_index

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and (self.current_step in (0, 1)):
            self.mouse_press_pos = event.pos()

    def mouseMoveEvent(self, event):
        if self.mouse_press_pos is not None and (self.current_step in (0, 1)):
            delta = event.pos() - self.mouse_press_pos
            delta.setY(0)
            new_pos = self.line.pos() + delta
            self.line.setPos(new_pos)
            self.mouse_press_pos = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and (self.current_step in (0, 1)):
            if self.current_action.final:
                return
            pos_in_original_image = QPointF(
                (1000 + self.line.pos().x()) * self.scale_x,
                (0 + self.line.pos().y()) * self.scale_y
            )
            action = None
            if self.current_step == 0:  # Вертикальный разрез
                action = Action(type='vertical_cut',
                                value=int(pos_in_original_image.x()),
                                final=False)
            elif self.current_step == 1:  # Горизонтальный разрез
                action = Action(type='horizontal_cut',
                                value=int(pos_in_original_image.y()),
                                final=False)
            self.add_action(action)
            self.mouse_press_pos = None
