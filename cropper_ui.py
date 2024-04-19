# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cropper_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 857)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_btn.setIcon(icon)
        self.save_btn.setIconSize(QtCore.QSize(32, 32))
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout.addWidget(self.save_btn)
        self.open_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_btn.sizePolicy().hasHeightForWidth())
        self.open_btn.setSizePolicy(sizePolicy)
        self.open_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/open.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open_btn.setIcon(icon1)
        self.open_btn.setIconSize(QtCore.QSize(32, 32))
        self.open_btn.setObjectName("open_btn")
        self.horizontalLayout.addWidget(self.open_btn)
        self.new_project_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_project_btn.sizePolicy().hasHeightForWidth())
        self.new_project_btn.setSizePolicy(sizePolicy)
        self.new_project_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/newfile.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_project_btn.setIcon(icon2)
        self.new_project_btn.setIconSize(QtCore.QSize(32, 32))
        self.new_project_btn.setObjectName("new_project_btn")
        self.horizontalLayout.addWidget(self.new_project_btn)
        self.check_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_btn.sizePolicy().hasHeightForWidth())
        self.check_btn.setSizePolicy(sizePolicy)
        self.check_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/check.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check_btn.setIcon(icon3)
        self.check_btn.setIconSize(QtCore.QSize(32, 32))
        self.check_btn.setObjectName("check_btn")
        self.horizontalLayout.addWidget(self.check_btn)
        self.check_all_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_all_btn.sizePolicy().hasHeightForWidth())
        self.check_all_btn.setSizePolicy(sizePolicy)
        self.check_all_btn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/check_all.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.check_all_btn.setIcon(icon4)
        self.check_all_btn.setIconSize(QtCore.QSize(32, 32))
        self.check_all_btn.setObjectName("check_all_btn")
        self.horizontalLayout.addWidget(self.check_all_btn)
        self.vert_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vert_btn.sizePolicy().hasHeightForWidth())
        self.vert_btn.setSizePolicy(sizePolicy)
        self.vert_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/vert.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vert_btn.setIcon(icon5)
        self.vert_btn.setIconSize(QtCore.QSize(32, 32))
        self.vert_btn.setObjectName("vert_btn")
        self.horizontalLayout.addWidget(self.vert_btn)
        self.horiz_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horiz_btn.sizePolicy().hasHeightForWidth())
        self.horiz_btn.setSizePolicy(sizePolicy)
        self.horiz_btn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/images/horiz.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.horiz_btn.setIcon(icon6)
        self.horiz_btn.setIconSize(QtCore.QSize(32, 32))
        self.horiz_btn.setObjectName("horiz_btn")
        self.horizontalLayout.addWidget(self.horiz_btn)
        self.crop_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.crop_btn.sizePolicy().hasHeightForWidth())
        self.crop_btn.setSizePolicy(sizePolicy)
        self.crop_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/images/crop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.crop_btn.setIcon(icon7)
        self.crop_btn.setIconSize(QtCore.QSize(32, 32))
        self.crop_btn.setObjectName("crop_btn")
        self.horizontalLayout.addWidget(self.crop_btn)
        self.angle_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.angle_btn.sizePolicy().hasHeightForWidth())
        self.angle_btn.setSizePolicy(sizePolicy)
        self.angle_btn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/images/angle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.angle_btn.setIcon(icon8)
        self.angle_btn.setIconSize(QtCore.QSize(32, 32))
        self.angle_btn.setObjectName("angle_btn")
        self.horizontalLayout.addWidget(self.angle_btn)
        self.rotate_clock_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_clock_btn.sizePolicy().hasHeightForWidth())
        self.rotate_clock_btn.setSizePolicy(sizePolicy)
        self.rotate_clock_btn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/clockwise_rotate.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_clock_btn.setIcon(icon9)
        self.rotate_clock_btn.setIconSize(QtCore.QSize(32, 32))
        self.rotate_clock_btn.setObjectName("rotate_clock_btn")
        self.horizontalLayout.addWidget(self.rotate_clock_btn)
        self.rotate_counter_clock_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rotate_counter_clock_btn.sizePolicy().hasHeightForWidth())
        self.rotate_counter_clock_btn.setSizePolicy(sizePolicy)
        self.rotate_counter_clock_btn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/counterclockwise_rotate.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rotate_counter_clock_btn.setIcon(icon10)
        self.rotate_counter_clock_btn.setIconSize(QtCore.QSize(32, 32))
        self.rotate_counter_clock_btn.setObjectName("rotate_counter_clock_btn")
        self.horizontalLayout.addWidget(self.rotate_counter_clock_btn)
        self.sciss_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sciss_btn.sizePolicy().hasHeightForWidth())
        self.sciss_btn.setSizePolicy(sizePolicy)
        self.sciss_btn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/images/scis.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sciss_btn.setIcon(icon11)
        self.sciss_btn.setIconSize(QtCore.QSize(32, 32))
        self.sciss_btn.setObjectName("sciss_btn")
        self.horizontalLayout.addWidget(self.sciss_btn)
        self.zoom_out_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_out_btn.sizePolicy().hasHeightForWidth())
        self.zoom_out_btn.setSizePolicy(sizePolicy)
        self.zoom_out_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/images/images/zoom_out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out_btn.setIcon(icon12)
        self.zoom_out_btn.setIconSize(QtCore.QSize(32, 32))
        self.zoom_out_btn.setObjectName("zoom_out_btn")
        self.horizontalLayout.addWidget(self.zoom_out_btn)
        self.zoom_in_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_in_btn.sizePolicy().hasHeightForWidth())
        self.zoom_in_btn.setSizePolicy(sizePolicy)
        self.zoom_in_btn.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/images/images/zoom_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in_btn.setIcon(icon13)
        self.zoom_in_btn.setIconSize(QtCore.QSize(32, 32))
        self.zoom_in_btn.setObjectName("zoom_in_btn")
        self.horizontalLayout.addWidget(self.zoom_in_btn)
        self.execute_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.execute_btn.sizePolicy().hasHeightForWidth())
        self.execute_btn.setSizePolicy(sizePolicy)
        self.execute_btn.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/run.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.execute_btn.setIcon(icon14)
        self.execute_btn.setIconSize(QtCore.QSize(32, 32))
        self.execute_btn.setObjectName("execute_btn")
        self.horizontalLayout.addWidget(self.execute_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.theme_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.theme_btn.sizePolicy().hasHeightForWidth())
        self.theme_btn.setSizePolicy(sizePolicy)
        self.theme_btn.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/images/images/night.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.theme_btn.setIcon(icon15)
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
        self.scroll_w = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.scroll_w.setObjectName("scroll_w")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.scroll_w)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.source_lb = QtWidgets.QLabel(self.scroll_w)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_lb.sizePolicy().hasHeightForWidth())
        self.source_lb.setSizePolicy(sizePolicy)
        self.source_lb.setObjectName("source_lb")
        self.horizontalLayout_4.addWidget(self.source_lb)
        self.verticalLayout_3.addWidget(self.scroll_w)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Обрезка изображений"))
        self.save_btn.setToolTip(_translate("MainWindow", "Сохранить проект"))
        self.open_btn.setToolTip(_translate("MainWindow", "Открыть проект"))
        self.new_project_btn.setToolTip(_translate("MainWindow", "Новый проект"))
        self.check_btn.setToolTip(_translate("MainWindow", "Пометить готовым"))
        self.check_all_btn.setToolTip(_translate("MainWindow", "Пометить все"))
        self.vert_btn.setToolTip(_translate("MainWindow", "Вертикальный разрез"))
        self.horiz_btn.setToolTip(_translate("MainWindow", "Горизонатльный разрез"))
        self.crop_btn.setToolTip(_translate("MainWindow", "Обрезка"))
        self.angle_btn.setToolTip(_translate("MainWindow", "Поворот на угол"))
        self.rotate_clock_btn.setToolTip(_translate("MainWindow", "Поворот вправо на 90 градусов"))
        self.rotate_counter_clock_btn.setToolTip(_translate("MainWindow", "Поворот влево на 90 градусов"))
        self.sciss_btn.setToolTip(_translate("MainWindow", "Разрезать"))
        self.zoom_out_btn.setToolTip(_translate("MainWindow", "Уменьшить масштаб"))
        self.zoom_in_btn.setToolTip(_translate("MainWindow", "Увеличить масштаб"))
        self.execute_btn.setToolTip(_translate("MainWindow", "Перейти на следующий этап"))
        self.theme_btn.setToolTip(_translate("MainWindow", "Переключение темы"))
        self.groupBox.setTitle(_translate("MainWindow", "Просмотр"))
        self.source_lb.setText(_translate("MainWindow", "TextLabel"))
        self.source_tw.setTabText(self.source_tw.indexOf(self.tab), _translate("MainWindow", "Исходник"))
import icons_rc
