# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rsrc/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 706)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_sframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_sframes.setMinimum(1)
        self.spinBox_sframes.setMaximum(1500)
        self.spinBox_sframes.setProperty("value", 1)
        self.spinBox_sframes.setObjectName("spinBox_sframes")
        self.gridLayout.addWidget(self.spinBox_sframes, 2, 1, 1, 1)
        self.spinBox_nframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_nframes.setMaximum(10000)
        self.spinBox_nframes.setProperty("value", 200)
        self.spinBox_nframes.setObjectName("spinBox_nframes")
        self.gridLayout.addWidget(self.spinBox_nframes, 1, 1, 1, 1)
        self.lcdNumber_sframes = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_sframes.setDigitCount(7)
        self.lcdNumber_sframes.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_sframes.setObjectName("lcdNumber_sframes")
        self.gridLayout.addWidget(self.lcdNumber_sframes, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 1)
        self.lcdNumber_thld_min = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_thld_min.setDigitCount(7)
        self.lcdNumber_thld_min.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_thld_min.setProperty("value", 0.0)
        self.lcdNumber_thld_min.setProperty("intValue", 0)
        self.lcdNumber_thld_min.setObjectName("lcdNumber_thld_min")
        self.gridLayout.addWidget(self.lcdNumber_thld_min, 6, 1, 1, 1)
        self.lcdNumber_thld_max = QtWidgets.QLCDNumber(self.groupBox)
        self.lcdNumber_thld_max.setSmallDecimalPoint(False)
        self.lcdNumber_thld_max.setDigitCount(7)
        self.lcdNumber_thld_max.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_thld_max.setProperty("value", 1000000.0)
        self.lcdNumber_thld_max.setProperty("intValue", 1000000)
        self.lcdNumber_thld_max.setObjectName("lcdNumber_thld_max")
        self.gridLayout.addWidget(self.lcdNumber_thld_max, 5, 1, 1, 1)
        self.checkBox_mask = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_mask.setObjectName("checkBox_mask")
        self.gridLayout.addWidget(self.checkBox_mask, 8, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.comboBox_window = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_window.setObjectName("comboBox_window")
        self.gridLayout.addWidget(self.comboBox_window, 11, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 0, 1, 1)
        self.checkBox_log = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_log.setObjectName("checkBox_log")
        self.gridLayout.addWidget(self.checkBox_log, 8, 1, 1, 1)
        self.comboBox_method = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_method.setObjectName("comboBox_method")
        self.gridLayout.addWidget(self.comboBox_method, 10, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 0, 1, 1)
        self.comboBox_color = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_color.setObjectName("comboBox_color")
        self.gridLayout.addWidget(self.comboBox_color, 13, 1, 1, 1)
        self.spinBox_lframes = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_lframes.setMaximum(10000)
        self.spinBox_lframes.setProperty("value", 1024)
        self.spinBox_lframes.setObjectName("spinBox_lframes")
        self.gridLayout.addWidget(self.spinBox_lframes, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 11, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 13, 0, 1, 1)
        self.checkBox_info = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_info.setObjectName("checkBox_info")
        self.gridLayout.addWidget(self.checkBox_info, 9, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_load_conf = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_load_conf.setObjectName("pushButton_load_conf")
        self.gridLayout_4.addWidget(self.pushButton_load_conf, 0, 1, 1, 1)
        self.pushButton_choose_file = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_choose_file.setObjectName("pushButton_choose_file")
        self.gridLayout_4.addWidget(self.pushButton_choose_file, 0, 0, 1, 1)
        self.pushButton_save_conf = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_save_conf.setObjectName("pushButton_save_conf")
        self.gridLayout_4.addWidget(self.pushButton_save_conf, 2, 1, 1, 1)
        self.pushButton_replot = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_replot.setObjectName("pushButton_replot")
        self.gridLayout_4.addWidget(self.pushButton_replot, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider_sframes = QtWidgets.QSlider(self.groupBox_3)
        self.verticalSlider_sframes.setStyleSheet("")
        self.verticalSlider_sframes.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_sframes.setInvertedAppearance(False)
        self.verticalSlider_sframes.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_sframes.setTickInterval(1)
        self.verticalSlider_sframes.setObjectName("verticalSlider_sframes")
        self.horizontalLayout.addWidget(self.verticalSlider_sframes)
        self.verticalSlider_thld_min = QtWidgets.QSlider(self.groupBox_3)
        self.verticalSlider_thld_min.setAutoFillBackground(False)
        self.verticalSlider_thld_min.setStyleSheet("")
        self.verticalSlider_thld_min.setMinimum(0)
        self.verticalSlider_thld_min.setMaximum(1000000)
        self.verticalSlider_thld_min.setSingleStep(10)
        self.verticalSlider_thld_min.setPageStep(1000)
        self.verticalSlider_thld_min.setProperty("value", 0)
        self.verticalSlider_thld_min.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_thld_min.setInvertedControls(False)
        self.verticalSlider_thld_min.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_thld_min.setTickInterval(0)
        self.verticalSlider_thld_min.setObjectName("verticalSlider_thld_min")
        self.horizontalLayout.addWidget(self.verticalSlider_thld_min)
        self.verticalSlider_thld_max = QtWidgets.QSlider(self.groupBox_3)
        self.verticalSlider_thld_max.setMaximum(1000000)
        self.verticalSlider_thld_max.setSingleStep(10)
        self.verticalSlider_thld_max.setPageStep(1000)
        self.verticalSlider_thld_max.setProperty("value", 1000000)
        self.verticalSlider_thld_max.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_thld_max.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_thld_max.setObjectName("verticalSlider_thld_max")
        self.horizontalLayout.addWidget(self.verticalSlider_thld_max)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mplWidget = MatplotLibWidget(self.groupBox_4)
        self.mplWidget.setObjectName("mplWidget")
        self.gridLayout_3.addWidget(self.mplWidget, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1114, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReplot = QtWidgets.QAction(MainWindow)
        self.actionReplot.setObjectName("actionReplot")
        self.actionChoose_file = QtWidgets.QAction(MainWindow)
        self.actionChoose_file.setObjectName("actionChoose_file")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionChoose_file)
        self.menuFile.addAction(self.actionReplot)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.spinBox_sframes.valueChanged['int'].connect(self.verticalSlider_sframes.setValue)
        self.verticalSlider_sframes.sliderMoved['int'].connect(self.spinBox_sframes.setValue)
        self.verticalSlider_thld_min.valueChanged['int'].connect(self.lcdNumber_thld_min.display)
        self.verticalSlider_thld_max.valueChanged['int'].connect(self.lcdNumber_thld_max.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.spinBox_lframes, self.spinBox_nframes)
        MainWindow.setTabOrder(self.spinBox_nframes, self.spinBox_sframes)
        MainWindow.setTabOrder(self.spinBox_sframes, self.comboBox_color)
        MainWindow.setTabOrder(self.comboBox_color, self.verticalSlider_sframes)
        MainWindow.setTabOrder(self.verticalSlider_sframes, self.verticalSlider_thld_min)
        MainWindow.setTabOrder(self.verticalSlider_thld_min, self.textBrowser)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iqgui"))
        self.groupBox.setTitle(_translate("MainWindow", "Navigation"))
        self.label_3.setText(_translate("MainWindow", "Starting frame:"))
        self.label_2.setText(_translate("MainWindow", "No. of frames:"))
        self.label_5.setText(_translate("MainWindow", "Method:"))
        self.checkBox_mask.setText(_translate("MainWindow", "Mask min."))
        self.label_7.setText(_translate("MainWindow", "Contrast max.:"))
        self.label.setText(_translate("MainWindow", "Starting time [s]:"))
        self.label_20.setText(_translate("MainWindow", "Points per frames:"))
        self.checkBox_log.setText(_translate("MainWindow", "Log"))
        self.label_4.setText(_translate("MainWindow", "Contrast min.:"))
        self.label_6.setText(_translate("MainWindow", "Window:"))
        self.label_21.setText(_translate("MainWindow", "Color map:"))
        self.checkBox_info.setText(_translate("MainWindow", "Info"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Actions"))
        self.pushButton_load_conf.setText(_translate("MainWindow", "Load Config"))
        self.pushButton_choose_file.setToolTip(_translate("MainWindow", "Open file [cmd] or [ct"))
        self.pushButton_choose_file.setText(_translate("MainWindow", "Choose File"))
        self.pushButton_save_conf.setText(_translate("MainWindow", "Save Config"))
        self.pushButton_replot.setToolTip(_translate("MainWindow", "Plot [return]"))
        self.pushButton_replot.setText(_translate("MainWindow", "Plot"))
        self.groupBox_2.setTitle(_translate("MainWindow", "File Info"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Sliders"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Plot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionReplot.setText(_translate("MainWindow", "Replot"))
        self.actionReplot.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionChoose_file.setText(_translate("MainWindow", "Choose file"))
        self.actionChoose_file.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

from matplotlibwidget import MatplotLibWidget
import gui_rc
