'''Модуль для обработки изображений и вырезания отдельных символов из них'''

# Нужно сделать базу данных проекта(создается при создании проекта) - структура:
# файлы -> ID(hash) -> Этапы -> каждый этап берет определенный ID на вход и
# применяет к нему операцию(кортеж) и на выходе 1,2... новых ID(На каждом этапе генерятся (только иконки?)
# или полностью изображения (тк ID уникальные можно хранить в одной папке) раскладывать в разные
#
# Нужно сделать обработку в виде проекта(папки) processing с
# подкаталогами для шагов обработки
# 1) rotates Пропускаем
# 2) vertical_cut (к именам файлов добавим vN(0, 1))
# 3) horizontal_cut (к именам файлов добавим hN(0, 1))
# 4) orientation
# 5) angle_adjust
# 6) word_select (к именам файлов добавим wN(00, 01, 02, ...))
# 7) letter_select(к именам файлов добавим lN(00, 01, 02, ...))
# 8) Формирование папки output в которой вырезанные буквы и цифры разложены по папкам 0 1 2 3 а б в ...
# Нажатие на кнопку действия создаёт(перезаписывает) файл(ы) в папке следующего этапа.
# К следующему этапу можно перейти если обработаны или подтверждены файлы текущего этапа
# Возможно отслеживать только изменения по действиям текущего этапа?
# Что делает возврат на предыдущий этап(ы)? при каких-то изменениях выделять цветом на следующих этапах?


import sys
import qdarkstyle
import traceback
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QGraphicsItem, QLabel, QGroupBox, QVBoxLayout, QGraphicsPixmapItem
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from PIL import ImageFont, ImageDraw
from cropper_ui import Ui_MainWindow
from classes import *
from functions import *


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.checked = None
        self.mouse_press_pos = None
        self.setupUi(self)
        self.theme = 'Dark'
        self.work_dir = None
        self.source_dir = None
        self.files = []
        self.thumbnails = []
        self.labels = []
        self.current_image_index = None
        self.check_list = []
        self.buttons = {
            "new_project": self.new_project_btn,
            "open": self.open_btn,
            "save": self.save_btn,
            "check_all": self.check_all_btn,
            "rotate_clock": self.rotate_clock_btn,
            "rotate_counter_clock": self.rotate_counter_clock_btn,
            "zoom_out": self.zoom_out_btn,
            "zoom_in": self.zoom_in_btn,
            "add_vertical_cut": self.add_vertical_cut_btn,
            "add_horizontal_cut": self.add_horizontal_cut_btn,
            "delete_cut": self.delete_cut_btn,
            "sciss_btn": self.sciss_btn,
            "previous": self.previous_btn,
            "next": self.next_btn
        }
        self.step_buttons = {
            "start": ["new_project", "open"],
            "vertical_cut": ["new_project", "open", "save", "check_all",
                             "zoom_in", "zoom_out", "add_vertical_cut",
                             "delete_cut", "sciss_btn", "next"],
            "horizontal_cut": ["new_project", "open", "save", "check_all",
                               "zoom_in", "zoom_out", "add_horizontal_cut",
                               "delete_cut", "sciss_btn", "previous", "next"],
            "orientation": ["new_project", "open", "save", "check_all",
                            "zoom_in", "zoom_out", "rotate_clock",
                            "rotate_counter_clock", "previous", "next"]
        }
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
        self.image_viewer = None
        self.scene = None
        self.pixmap = None
        self.project = None
        self.show_buttons()

    def show_buttons(self):
        if self.project is None:
            step_name = 'start'
        else:
            step_name = STEPS[self.project.current_step]
        for name, button in self.buttons.items():
            if name in self.step_buttons.get(step_name, []):
                button.show()  # Показываем кнопку
            else:
                button.hide()  # Скрываем кнопку

    def check_all(self):
        for check_box in self.check_list:
            check_box.setChecked(True)

    def add_vertical(self):
        if self.image_viewer is not None:
            self.image_viewer.add_line()
            self.image_sa.show()
            self.sciss_btn.setEnabled(True)

    def create_new_project(self):
        self.project = Project()
        if not self.project.new_project(self):
            return
        self.work_dir = self.project.work_dir + '/processing/' + self.project.steps[self.project.current_step]
        self.files = self.project.load_current_files()
        self.thumbnails = self.project.get_current_thumbnails()
        self.show_thumbnails()
        self.setWindowTitle('Обработка изображений - вертикальный разрез')
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
        self.checked = self.project.get_current_check_list()
        self.show_thumbnails(self.checked)
        self.setWindowTitle('Обработка изображений - вертикальный разрез')
        self.show_buttons()

    def highlight_thumbnail(self, index):
        # Убираем выделение у всех остальных thumbnails
        for label in self.labels:
            label.setStyleSheet("border: none;")

        # Выделяем текущий thumbnail
        if index >= 0 and index < len(self.labels):
            self.labels[index].setStyleSheet("border: 2px solid green;")  # Рамка красного цвета

    def show_thumbnails(self, checked=None):
        if checked is None:
            checked = []
        if len(self.thumbnails) > 0:
            v_layout = QVBoxLayout()
            group_box = QGroupBox()
            num = 1
            self.labels.clear()
            for file in self.thumbnails:
                mini_v_layout = QVBoxLayout()
                label_num = QLabel(f'{num}:')
                check_box = QCheckBox()
                if len(checked) > num - 1:
                    check_box.setChecked(checked[num - 1])
                self.check_list.append(check_box)
                num += 1
                label = Mylabel(self)
                label.setPixmap(QPixmap(file).scaled(200, 400, QtCore.Qt.KeepAspectRatio))
                self.labels.append(label)
                v_sp = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
                mini_v_layout.addWidget(label_num)
                mini_v_layout.addWidget(check_box)
                mini_v_layout.addItem(v_sp)
                h_layout = QHBoxLayout()
                h_layout.addLayout(mini_v_layout)
                h_layout.addWidget(label)
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
                self.highlight_thumbnail(i)
                self.image_viewer = self.project.create_viewer(file, i)
                self.image_sa.setWidget(self.image_viewer)
                self.image_sa.show()

    def apply_action_to_image(self, action: Action, image):
        """Применяет операцию к изображению."""
        updated_image = image
        if action.type == 'vertical_cut':
            # Логика обрезки изображения
            pass
        elif action.type == 'crop':
            # Логика кадрирования изображения
            pass
        elif action.type == 'rotate':
            # Логика поворота изображения
            pass
        else:
            raise ValueError(f'Неизвестный тип операции: {action.type}')

        # Возвращаем обновленное изображение
        return updated_image

    def update_thumbnail(self, index):
        """Обновляет иконку по индексу."""
        file = self.files[index]
        image = Image.open(file)
        original_width = image.width
        original_height = image.height
        image.thumbnail((400, 400))
        if index in self.project.actions:
            action = self.project.actions[index]
            if action.type == 'vertical_cut':
                scale_x = original_width / image.width
                x = action.value / scale_x
                draw = ImageDraw.Draw(image)
                draw.line((x, 0, x, image.height), fill=(255, 0, 0), width=1)

        new_name = self.work_dir + '/thumbnails/' + os.path.basename(file)
        image.save(new_name)
        self.thumbnails.append(new_name)
        thumbnail = self.thumbnails[index]
        thumbnail.setPixmap(image)

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
        pass
        # self.rotates[self.current_image_index] += 90
        # if self.rotates[self.current_image_index] >= 0:
        #     self.write_on_thumbnails(f'Right {self.rotates[self.current_image_index]}')
        # else:
        #     self.write_on_thumbnails(f'Left {-self.rotates[self.current_image_index]}')

    def rotate_left(self):
        pass
        # self.rotates[self.current_image_index] -= 90
        # # self.rotates[self.current_image_index] %= 360
        # if self.rotates[self.current_image_index] >= 0:
        #     self.write_on_thumbnails(f'Right {self.rotates[self.current_image_index]}')
        # else:
        #     self.write_on_thumbnails(f'Left {-self.rotates[self.current_image_index]}')

    def write_on_thumbnails(self, text):
        im = Image.open(self.thumbnails[self.current_image_index])
        font = ImageFont.truetype('./data/consolas.ttf', size=42)
        draw_text = ImageDraw.Draw(im)
        draw_text.text(
            (5, 5),
            text,
            font=font,
            fill='#FF0000'
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
        # checked = []
        # actions = []
        # for cb in self.check_list:
        #     checked.append(cb.isChecked())
        # if self.project.current_step == 0:
        #     actions = self.actions
        # self.project.set_current_action_steps(actions, checked)
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
