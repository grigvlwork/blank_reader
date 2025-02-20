# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cropper_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 857)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/character.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_project_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_project_btn.sizePolicy().hasHeightForWidth())
        self.new_project_btn.setSizePolicy(sizePolicy)
        self.new_project_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/newfile.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_project_btn.setIcon(icon1)
        self.new_project_btn.setIconSize(QtCore.QSize(32, 32))
        self.new_project_btn.setObjectName("new_project_btn")
        self.horizontalLayout.addWidget(self.new_project_btn)
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_btn.sizePolicy().hasHeightForWidth())
        self.open_btn.setSizePolicy(sizePolicy)
        self.open_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_btn.setIcon(icon2)
        self.open_btn.setIconSize(QtCore.QSize(32, 32))
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon3)
        self.save_btn.setIconSize(QtCore.QSize(32, 32))
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.check_all_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_all_btn.sizePolicy().hasHeightForWidth())
        self.check_all_btn.setSizePolicy(sizePolicy)
        self.check_all_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/checklist.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check_all_btn.setIcon(icon4)
        self.check_all_btn.setIconSize(QtCore.QSize(32, 32))
        self.check_all_btn.setObjectName("check_all_btn")
        self.horizontalLayout.addWidget(self.check_all_btn)
        self.flip_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flip_btn.sizePolicy().hasHeightForWidth())
        self.flip_btn.setSizePolicy(sizePolicy)
        self.flip_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/flip_thumb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.flip_btn.setIcon(icon5)
        self.flip_btn.setIconSize(QtCore.QSize(32, 32))
        self.flip_btn.setObjectName("flip_btn")
        self.horizontalLayout.addWidget(self.flip_btn)
        self.rotate_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_btn.sizePolicy().hasHeightForWidth())
        self.rotate_btn.setSizePolicy(sizePolicy)
        self.rotate_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/angle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_btn.setIcon(icon6)
        self.rotate_btn.setIconSize(QtCore.QSize(32, 32))
        self.rotate_btn.setObjectName("rotate_btn")
        self.horizontalLayout.addWidget(self.rotate_btn)
        self.add_grid_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_grid_btn.sizePolicy().hasHeightForWidth())
        self.add_grid_btn.setSizePolicy(sizePolicy)
        self.add_grid_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/add_grid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_grid_btn.setIcon(icon7)
        self.add_grid_btn.setIconSize(QtCore.QSize(32, 32))
        self.add_grid_btn.setObjectName("add_grid_btn")
        self.horizontalLayout.addWidget(self.add_grid_btn)
        self.contour_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contour_btn.sizePolicy().hasHeightForWidth())
        self.contour_btn.setSizePolicy(sizePolicy)
        self.contour_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/border.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.contour_btn.setIcon(icon8)
        self.contour_btn.setIconSize(QtCore.QSize(32, 32))
        self.contour_btn.setObjectName("contour_btn")
        self.horizontalLayout.addWidget(self.contour_btn)
        self.confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_btn.sizePolicy().hasHeightForWidth())
        self.confirm_btn.setSizePolicy(sizePolicy)
        self.confirm_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/images/yes_black.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.confirm_btn.setIcon(icon9)
        self.confirm_btn.setIconSize(QtCore.QSize(32, 32))
        self.confirm_btn.setObjectName("confirm_btn")
        self.horizontalLayout.addWidget(self.confirm_btn)
        self.add_vertical_cut_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_vertical_cut_btn.sizePolicy().hasHeightForWidth())
        self.add_vertical_cut_btn.setSizePolicy(sizePolicy)
        self.add_vertical_cut_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/vertical_cut.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_vertical_cut_btn.setIcon(icon10)
        self.add_vertical_cut_btn.setIconSize(QtCore.QSize(32, 32))
        self.add_vertical_cut_btn.setObjectName("add_vertical_cut_btn")
        self.horizontalLayout.addWidget(self.add_vertical_cut_btn)
        self.add_horizontal_cut_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_horizontal_cut_btn.sizePolicy().hasHeightForWidth())
        self.add_horizontal_cut_btn.setSizePolicy(sizePolicy)
        self.add_horizontal_cut_btn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/horizontal_cut.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_horizontal_cut_btn.setIcon(icon11)
        self.add_horizontal_cut_btn.setIconSize(QtCore.QSize(32, 32))
        self.add_horizontal_cut_btn.setObjectName("add_horizontal_cut_btn")
        self.horizontalLayout.addWidget(self.add_horizontal_cut_btn)
        self.delete_cut_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_cut_btn.sizePolicy().hasHeightForWidth())
        self.delete_cut_btn.setSizePolicy(sizePolicy)
        self.delete_cut_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/delete_cuts.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_cut_btn.setIcon(icon12)
        self.delete_cut_btn.setIconSize(QtCore.QSize(32, 32))
        self.delete_cut_btn.setObjectName("delete_cut_btn")
        self.horizontalLayout.addWidget(self.delete_cut_btn)
        self.sciss_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sciss_btn.sizePolicy().hasHeightForWidth())
        self.sciss_btn.setSizePolicy(sizePolicy)
        self.sciss_btn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/images/scis.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sciss_btn.setIcon(icon13)
        self.sciss_btn.setIconSize(QtCore.QSize(32, 32))
        self.sciss_btn.setObjectName("sciss_btn")
        self.horizontalLayout.addWidget(self.sciss_btn)
        self.previous_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_btn.sizePolicy().hasHeightForWidth())
        self.previous_btn.setSizePolicy(sizePolicy)
        self.previous_btn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/previous.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_btn.setIcon(icon14)
        self.previous_btn.setIconSize(QtCore.QSize(32, 32))
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout.addWidget(self.previous_btn)
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy)
        self.next_btn.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/next.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon15)
        self.next_btn.setIconSize(QtCore.QSize(32, 32))
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout.addWidget(self.next_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.theme_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme_btn.sizePolicy().hasHeightForWidth())
        self.theme_btn.setSizePolicy(sizePolicy)
        self.theme_btn.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/images/images/night.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.theme_btn.setIcon(icon16)
        self.theme_btn.setIconSize(QtCore.QSize(32, 32))
        self.theme_btn.setObjectName("theme_btn")
        self.horizontalLayout.addWidget(self.theme_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.source_tw = QtWidgets.QTabWidget(self.centralwidget)
        self.source_tw.setObjectName("source_tw")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.thumbnails_sa = QtWidgets.QScrollArea(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnails_sa.sizePolicy().hasHeightForWidth())
        self.thumbnails_sa.setSizePolicy(sizePolicy)
        self.thumbnails_sa.setMinimumSize(QtCore.QSize(300, 0))
        self.thumbnails_sa.setWidgetResizable(True)
        self.thumbnails_sa.setObjectName("thumbnails_sa")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 723))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.thumbnails_sa.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.thumbnails_sa)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image_sa = QtWidgets.QScrollArea(self.groupBox)
        self.image_sa.setWidgetResizable(True)
        self.image_sa.setObjectName("image_sa")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 738, 690))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.source_lb = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_lb.sizePolicy().hasHeightForWidth())
        self.source_lb.setSizePolicy(sizePolicy)
        self.source_lb.setObjectName("source_lb")
        self.verticalLayout_3.addWidget(self.source_lb)
        self.image_sa.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.image_sa)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.source_tw.addTab(self.tab, "")
        self.horizontalLayout_2.addWidget(self.source_tw)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.source_tw.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обработка изображений"))
        self.new_project_btn.setToolTip(_translate("MainWindow", "Новый проект"))
        self.open_btn.setToolTip(_translate("MainWindow", "Открыть проект"))
        self.save_btn.setToolTip(_translate("MainWindow", "Сохранить проект"))
        self.check_all_btn.setToolTip(_translate("MainWindow", "Пометить все"))
        self.flip_btn.setToolTip(_translate("MainWindow", "Поворот на 180 градусов"))
        self.rotate_btn.setToolTip(_translate("MainWindow", "Поворот изображения"))
        self.add_grid_btn.setToolTip(_translate("MainWindow", "Добавить сетку"))
        self.contour_btn.setToolTip(_translate("MainWindow", "Найти контуры"))
        self.confirm_btn.setToolTip(_translate("MainWindow", "Подвердить "))
        self.add_vertical_cut_btn.setToolTip(_translate("MainWindow", "Добавить вертикальный разрез"))
        self.add_horizontal_cut_btn.setToolTip(_translate("MainWindow", "Добавить горизонтальный разрез"))
        self.delete_cut_btn.setToolTip(_translate("MainWindow", "Удалить добавленные разрезы"))
        self.sciss_btn.setToolTip(_translate("MainWindow", "Разрезать"))
        self.previous_btn.setToolTip(_translate("MainWindow", "Перейти на предыдущий этап"))
        self.next_btn.setToolTip(_translate("MainWindow", "Перейти на следующий этап"))
        self.theme_btn.setToolTip(_translate("MainWindow", "Переключение темы"))
        self.groupBox.setTitle(_translate("MainWindow", "Просмотр"))
        self.source_lb.setText(_translate("MainWindow", "TextLabel"))
        self.source_tw.setTabText(self.source_tw.indexOf(self.tab), _translate("MainWindow", "Исходник"))
import icons_rc
