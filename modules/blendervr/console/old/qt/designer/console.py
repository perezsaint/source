# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/damien/sources/blenderVR/trunk/modules/blendervr/console/qt/designer/console.ui'
#
# Created: Mon Oct  6 13:53:38 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_console(object):
    def setupUi(self, console):
        console.setObjectName(_fromUtf8("console"))
        console.resize(671, 628)
        self.main_console = QtGui.QWidget(console)
        self.main_console.setEnabled(True)
        self.main_console.setMinimumSize(QtCore.QSize(671, 0))
        self.main_console.setStyleSheet(_fromUtf8(""))
        self.main_console.setObjectName(_fromUtf8("main_console"))
        self.gridLayout_5 = QtGui.QGridLayout(self.main_console)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox = QtGui.QGroupBox(self.main_console)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.select_screen_set = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_screen_set.sizePolicy().hasHeightForWidth())
        self.select_screen_set.setSizePolicy(sizePolicy)
        self.select_screen_set.setObjectName(_fromUtf8("select_screen_set"))
        self.horizontalLayout.addWidget(self.select_screen_set)
        self.set_screen_set = QtGui.QPushButton(self.groupBox)
        self.set_screen_set.setObjectName(_fromUtf8("set_screen_set"))
        self.horizontalLayout.addWidget(self.set_screen_set)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.current_screen_set = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.current_screen_set.setFont(font)
        self.current_screen_set.setObjectName(_fromUtf8("current_screen_set"))
        self.horizontalLayout.addWidget(self.current_screen_set)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.main_console)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.blender_file = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blender_file.sizePolicy().hasHeightForWidth())
        self.blender_file.setSizePolicy(sizePolicy)
        self.blender_file.setObjectName(_fromUtf8("blender_file"))
        self.gridLayout_2.addWidget(self.blender_file, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.processor_file = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processor_file.sizePolicy().hasHeightForWidth())
        self.processor_file.setSizePolicy(sizePolicy)
        self.processor_file.setObjectName(_fromUtf8("processor_file"))
        self.gridLayout_2.addWidget(self.processor_file, 1, 1, 1, 1)
        self.link_processor_to_blender = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.link_processor_to_blender.sizePolicy().hasHeightForWidth())
        self.link_processor_to_blender.setSizePolicy(sizePolicy)
        self.link_processor_to_blender.setCheckable(True)
        self.link_processor_to_blender.setObjectName(_fromUtf8("link_processor_to_blender"))
        self.gridLayout_2.addWidget(self.link_processor_to_blender, 0, 2, 2, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 3, 0, 1, 1)
        self.main_tab = QtGui.QTabWidget(self.main_console)
        self.main_tab.setObjectName(_fromUtf8("main_tab"))
        self.configuration_tab = QtGui.QWidget()
        self.configuration_tab.setObjectName(_fromUtf8("configuration_tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.configuration_tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.configuration_box = QtGui.QGroupBox(self.configuration_tab)
        self.configuration_box.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configuration_box.sizePolicy().hasHeightForWidth())
        self.configuration_box.setSizePolicy(sizePolicy)
        self.configuration_box.setObjectName(_fromUtf8("configuration_box"))
        self.gridLayout_4 = QtGui.QGridLayout(self.configuration_box)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.configuration_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.configuration_file = QtGui.QPushButton(self.configuration_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configuration_file.sizePolicy().hasHeightForWidth())
        self.configuration_file.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setKerning(False)
        self.configuration_file.setFont(font)
        self.configuration_file.setAutoDefault(False)
        self.configuration_file.setFlat(False)
        self.configuration_file.setObjectName(_fromUtf8("configuration_file"))
        self.gridLayout.addWidget(self.configuration_file, 0, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.configuration_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 5, 1)
        self.configuration_paths = QtGui.QListWidget(self.configuration_box)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configuration_paths.sizePolicy().hasHeightForWidth())
        self.configuration_paths.setSizePolicy(sizePolicy)
        self.configuration_paths.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.configuration_paths.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.configuration_paths.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.configuration_paths.setObjectName(_fromUtf8("configuration_paths"))
        self.gridLayout.addWidget(self.configuration_paths, 2, 1, 5, 1)
        self.clear_configuration_paths = QtGui.QPushButton(self.configuration_box)
        self.clear_configuration_paths.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.clear_configuration_paths.setObjectName(_fromUtf8("clear_configuration_paths"))
        self.gridLayout.addWidget(self.clear_configuration_paths, 6, 2, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 2, 1, 1)
        self.load_configuration_file = QtGui.QPushButton(self.configuration_box)
        self.load_configuration_file.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_configuration_file.sizePolicy().hasHeightForWidth())
        self.load_configuration_file.setSizePolicy(sizePolicy)
        self.load_configuration_file.setObjectName(_fromUtf8("load_configuration_file"))
        self.gridLayout.addWidget(self.load_configuration_file, 1, 1, 1, 2)
        self.add_configuration_path = QtGui.QPushButton(self.configuration_box)
        self.add_configuration_path.setObjectName(_fromUtf8("add_configuration_path"))
        self.gridLayout.addWidget(self.add_configuration_path, 2, 2, 1, 1)
        self.remove_configuration_path = QtGui.QPushButton(self.configuration_box)
        self.remove_configuration_path.setObjectName(_fromUtf8("remove_configuration_path"))
        self.gridLayout.addWidget(self.remove_configuration_path, 3, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.configuration_box)
        self.main_tab.addTab(self.configuration_tab, _fromUtf8(""))
        self.run_tab = QtGui.QWidget()
        self.run_tab.setObjectName(_fromUtf8("run_tab"))
        self.gridLayout_8 = QtGui.QGridLayout(self.run_tab)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.start = QtGui.QPushButton(self.run_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start.setFont(font)
        self.start.setObjectName(_fromUtf8("start"))
        self.gridLayout_8.addWidget(self.start, 0, 0, 1, 1)
        self.status = QtGui.QLabel(self.run_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.status.setFont(font)
        self.status.setAutoFillBackground(True)
        self.status.setFrameShape(QtGui.QFrame.StyledPanel)
        self.status.setText(_fromUtf8(""))
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName(_fromUtf8("status"))
        self.gridLayout_8.addWidget(self.status, 0, 2, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.run_tab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_12 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName(_fromUtf8("gridLayout_12"))
        self.gridLayout_11 = QtGui.QGridLayout()
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.log_window = QtGui.QTextEdit(self.groupBox_3)
        self.log_window.setReadOnly(True)
        self.log_window.setObjectName(_fromUtf8("log_window"))
        self.gridLayout_11.addWidget(self.log_window, 1, 0, 1, 2)
        self.log_level_selector = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_level_selector.sizePolicy().hasHeightForWidth())
        self.log_level_selector.setSizePolicy(sizePolicy)
        self.log_level_selector.setObjectName(_fromUtf8("log_level_selector"))
        self.gridLayout_11.addWidget(self.log_level_selector, 0, 1, 1, 1)
        self.clear_log = QtGui.QPushButton(self.groupBox_3)
        self.clear_log.setObjectName(_fromUtf8("clear_log"))
        self.gridLayout_11.addWidget(self.clear_log, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_3, 1, 0, 1, 4)
        self.stop = QtGui.QPushButton(self.run_tab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stop.setFont(font)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.gridLayout_8.addWidget(self.stop, 0, 1, 1, 1)
        self.main_tab.addTab(self.run_tab, _fromUtf8(""))
        self.gridLayout_5.addWidget(self.main_tab, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.line_2 = QtGui.QFrame(self.main_console)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_2.addWidget(self.line_2)
        self.label_7 = QtGui.QLabel(self.main_console)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.nb_stopped = QtGui.QLabel(self.main_console)
        self.nb_stopped.setObjectName(_fromUtf8("nb_stopped"))
        self.horizontalLayout_2.addWidget(self.nb_stopped)
        self.line_3 = QtGui.QFrame(self.main_console)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_2.addWidget(self.line_3)
        self.label_9 = QtGui.QLabel(self.main_console)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.nb_starting = QtGui.QLabel(self.main_console)
        self.nb_starting.setObjectName(_fromUtf8("nb_starting"))
        self.horizontalLayout_2.addWidget(self.nb_starting)
        self.line_4 = QtGui.QFrame(self.main_console)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_2.addWidget(self.line_4)
        self.label_11 = QtGui.QLabel(self.main_console)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_2.addWidget(self.label_11)
        self.nb_running = QtGui.QLabel(self.main_console)
        self.nb_running.setObjectName(_fromUtf8("nb_running"))
        self.horizontalLayout_2.addWidget(self.nb_running)
        self.line_5 = QtGui.QFrame(self.main_console)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout_2.addWidget(self.line_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        console.setCentralWidget(self.main_console)
        self.menubar = QtGui.QMenuBar(console)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
        self.menuScreens = QtGui.QMenu(self.menuWindows)
        self.menuScreens.setObjectName(_fromUtf8("menuScreens"))
        console.setMenuBar(self.menubar)
        self.status_bar = QtGui.QStatusBar(console)
        self.status_bar.setObjectName(_fromUtf8("status_bar"))
        console.setStatusBar(self.status_bar)
        self.menuQuit = QtGui.QAction(console)
        self.menuQuit.setObjectName(_fromUtf8("menuQuit"))
        self.all_screens = QtGui.QAction(console)
        self.all_screens.setCheckable(True)
        self.all_screens.setObjectName(_fromUtf8("all_screens"))
        self.menuOptions = QtGui.QAction(console)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuProcessor = QtGui.QAction(console)
        self.menuProcessor.setCheckable(True)
        self.menuProcessor.setObjectName(_fromUtf8("menuProcessor"))
        self.menuFile.addAction(self.menuQuit)
        self.menuWindows.addAction(self.menuScreens.menuAction())
        self.menuWindows.addSeparator()
        self.menuWindows.addAction(self.menuProcessor)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())

        self.retranslateUi(console)
        self.main_tab.setCurrentIndex(0)
        QtCore.QObject.connect(self.clear_configuration_paths, QtCore.SIGNAL(_fromUtf8("clicked()")), self.configuration_paths.clear)
        QtCore.QObject.connect(self.clear_log, QtCore.SIGNAL(_fromUtf8("clicked()")), self.log_window.clear)
        QtCore.QMetaObject.connectSlotsByName(console)

    def retranslateUi(self, console):
        console.setWindowTitle(QtGui.QApplication.translate("console", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("console", "Screen sets:", None, QtGui.QApplication.UnicodeUTF8))
        self.set_screen_set.setText(QtGui.QApplication.translate("console", "> Load screen set", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("console", "Current  :", None, QtGui.QApplication.UnicodeUTF8))
        self.current_screen_set.setText(QtGui.QApplication.translate("console", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("console", "Simulation file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("console", ".blend", None, QtGui.QApplication.UnicodeUTF8))
        self.blender_file.setText(QtGui.QApplication.translate("console", "Set ...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("console", ".processor.py", None, QtGui.QApplication.UnicodeUTF8))
        self.processor_file.setText(QtGui.QApplication.translate("console", "Set ...", None, QtGui.QApplication.UnicodeUTF8))
        self.link_processor_to_blender.setText(QtGui.QApplication.translate("console", "NameLink", None, QtGui.QApplication.UnicodeUTF8))
        self.configuration_box.setTitle(QtGui.QApplication.translate("console", "Configuration file and additional search paths:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("console", "File:", None, QtGui.QApplication.UnicodeUTF8))
        self.configuration_file.setText(QtGui.QApplication.translate("console", "Select config file (.xml)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("console", "Paths:", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_configuration_paths.setText(QtGui.QApplication.translate("console", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.load_configuration_file.setText(QtGui.QApplication.translate("console", "> Load configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.add_configuration_path.setText(QtGui.QApplication.translate("console", "Add ..", None, QtGui.QApplication.UnicodeUTF8))
        self.remove_configuration_path.setText(QtGui.QApplication.translate("console", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.main_tab.setTabText(self.main_tab.indexOf(self.configuration_tab), QtGui.QApplication.translate("console", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setText(QtGui.QApplication.translate("console", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("console", "Log window:", None, QtGui.QApplication.UnicodeUTF8))
        self.clear_log.setText(QtGui.QApplication.translate("console", "clear", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("console", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.main_tab.setTabText(self.main_tab.indexOf(self.run_tab), QtGui.QApplication.translate("console", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("console", "Stopped:", None, QtGui.QApplication.UnicodeUTF8))
        self.nb_stopped.setText(QtGui.QApplication.translate("console", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("console", "Starting:", None, QtGui.QApplication.UnicodeUTF8))
        self.nb_starting.setText(QtGui.QApplication.translate("console", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("console", "Running:", None, QtGui.QApplication.UnicodeUTF8))
        self.nb_running.setText(QtGui.QApplication.translate("console", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("console", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindows.setTitle(QtGui.QApplication.translate("console", "Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.menuScreens.setTitle(QtGui.QApplication.translate("console", "Screens", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setText(QtGui.QApplication.translate("console", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuQuit.setShortcut(QtGui.QApplication.translate("console", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.all_screens.setText(QtGui.QApplication.translate("console", "All screens", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setText(QtGui.QApplication.translate("console", "options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProcessor.setText(QtGui.QApplication.translate("console", "Processor window", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProcessor.setShortcut(QtGui.QApplication.translate("console", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))


class console(QtGui.QMainWindow, Ui_console):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QMainWindow.__init__(self, parent, f)

        self.setupUi(self)
