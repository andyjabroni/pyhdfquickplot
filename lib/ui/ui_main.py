# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created: Fri Feb 07 12:50:12 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1041, 661)
        MainWindow.setStyleSheet(_fromUtf8("#centralwidget {    background-color:#333; }\n"
"#bg_browser { background-color:#444; }\n"
"\n"
"QCheckBox { spacing:10px; font-size: 14px; color:#fff; font-weight:bold; }\n"
"QCheckBox:hover { color:red; }\n"
"\n"
"#label_programtitle { font-size:28px; color:white; font-style:italic; font-weight:bold; }\n"
"\n"
"#btn_minimize { font-size:16px; background-color:orange; border:0px; color:black; font-weight:bold; }\n"
"#btn_minimize:hover { background-color:#fc5700; }\n"
"#btn_exit {    font-size:16px; background-color:orange; border:0px; color:black; font-weight:bold; }\n"
"#btn_exit:hover { background-color:#fc5700; }\n"
"\n"
"#btn_openfile { font-size:12px; background-color:orange; border:0px; color:black; font-weight:bold; }\n"
"#btn_openfile:hover { background-color:#fc5700; }\n"
"#value_progress { font-size:12px; color:white; font-weight:bold; }\n"
"#btn_recentlyopened { font-size:12px; background-color:orange; border:0px; color:black; font-weight:bold; }\n"
"#btn_recentlyopened:hover { background-color:#fc5700; }\n"
"\n"
"/*#mplwidget { border-radius:8px;}*/\n"
"\n"
"#bg_hdftree { border-radius:8px; background-color:black; }\n"
"#list { color:#fff; font-size: 14px; font-weight: bold; background-color:#000; alternate-background-color: #333; selection-color:#fff; selection-background-color:red; }\n"
"\n"
"#label_currenthdf{ font-size:16px; color:white; font-style:italic; font-weight:bold; }\n"
"#label_avtimerange { font-size:14px; font-weight:bold; color:#fc5700; }\n"
"#value_timerange { font-size:14px; font-weight:bold; color:white; }\n"
"#label_avindexrange { font-size:14px; font-weight:bold; color:#fc5700; }\n"
"#value_indexrange { font-size:14px; font-weight:bold; color:white; }\n"
"QSlider::groove:horizontal {\n"
"    border-radius:5px;\n"
"    height: 18px;\n"
"    background-color:#B1B1B1;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    border:2px solid #000;\n"
"    border-radius:5px;\n"
"    width:20px;\n"
"    margin:2px;\n"
"    background-color:#444;\n"
"}\n"
"\n"
"#bg_controls { border-radius:8px; background-color:black; }\n"
"#label_plotindexrange { font-size:16px; color:white; font-style:italic; font-weight:bold; }\n"
"#label_startindex { font-size:14px; font-weight:bold; color:#fc5700; }\n"
"#lineedit_startindex { font-size:14px; border:0px; font-weight:bold; color:black; }\n"
"#lineedit_startindex:hover { border:1px solid orange; background-color:#fc5700; color:white; }\n"
"#value_startindex { font-size:14px; font-weight:bold; color:white; }\n"
"#label_stopindex { font-size:14px; font-weight:bold; color:#fc5700; }\n"
"#lineedit_stopindex { font-size:14px; border:0px; font-weight:bold; color:black; }\n"
"#lineedit_stopindex:hover { border:1px solid orange; background-color:#fc5700; color:white; }\n"
"#value_stopindex { font-size:14px; font-weight:bold; color:white; }\n"
"\n"
"#btn_reset { font-size:14px; background-color:orange; border:0px; color:black; font-weight:bold; }\n"
"#btn_reset:hover { background-color:#fc5700; }\n"
"#btn_plot { font-size:14px; background-color:orange; border:0px; color:black; font-weight:bold; }\n"
"#btn_plot:hover { background-color:#fc5700; }"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bg_browser = QtGui.QLabel(self.centralwidget)
        self.bg_browser.setGeometry(QtCore.QRect(10, 40, 1021, 611))
        self.bg_browser.setText(_fromUtf8(""))
        self.bg_browser.setObjectName(_fromUtf8("bg_browser"))
        self.checkbox_separate = QtGui.QCheckBox(self.centralwidget)
        self.checkbox_separate.setGeometry(QtCore.QRect(410, 620, 131, 22))
        self.checkbox_separate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkbox_separate.setObjectName(_fromUtf8("checkbox_separate"))
        self.btn_reset = QtGui.QPushButton(self.centralwidget)
        self.btn_reset.setGeometry(QtCore.QRect(560, 620, 71, 21))
        self.btn_reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_reset.setObjectName(_fromUtf8("btn_reset"))
        self.checkbox_3d = QtGui.QCheckBox(self.centralwidget)
        self.checkbox_3d.setGeometry(QtCore.QRect(320, 620, 81, 22))
        self.checkbox_3d.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkbox_3d.setObjectName(_fromUtf8("checkbox_3d"))
        self.btn_plot = QtGui.QPushButton(self.centralwidget)
        self.btn_plot.setGeometry(QtCore.QRect(640, 620, 71, 21))
        self.btn_plot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_plot.setObjectName(_fromUtf8("btn_plot"))
        self.mplwidget = MatplotlibWidget(self.centralwidget)
        self.mplwidget.setGeometry(QtCore.QRect(280, 50, 741, 421))
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.label_programtitle = QtGui.QLabel(self.centralwidget)
        self.label_programtitle.setGeometry(QtCore.QRect(10, 0, 1021, 41))
        self.label_programtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_programtitle.setObjectName(_fromUtf8("label_programtitle"))
        self.btn_minimize = QtGui.QPushButton(self.centralwidget)
        self.btn_minimize.setGeometry(QtCore.QRect(839, 10, 111, 21))
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setFlat(True)
        self.btn_minimize.setObjectName(_fromUtf8("btn_minimize"))
        self.btn_exit = QtGui.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(960, 10, 71, 21))
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setFlat(True)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.bg_controls = QtGui.QLabel(self.centralwidget)
        self.bg_controls.setGeometry(QtCore.QRect(20, 480, 1001, 131))
        self.bg_controls.setText(_fromUtf8(""))
        self.bg_controls.setObjectName(_fromUtf8("bg_controls"))
        self.lineedit_startindex = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_startindex.setGeometry(QtCore.QRect(931, 530, 71, 21))
        self.lineedit_startindex.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineedit_startindex.setText(_fromUtf8(""))
        self.lineedit_startindex.setObjectName(_fromUtf8("lineedit_startindex"))
        self.lineedit_stopindex = QtGui.QLineEdit(self.centralwidget)
        self.lineedit_stopindex.setGeometry(QtCore.QRect(931, 580, 71, 21))
        self.lineedit_stopindex.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineedit_stopindex.setText(_fromUtf8(""))
        self.lineedit_stopindex.setObjectName(_fromUtf8("lineedit_stopindex"))
        self.label_startindex = QtGui.QLabel(self.centralwidget)
        self.label_startindex.setGeometry(QtCore.QRect(440, 510, 111, 21))
        self.label_startindex.setObjectName(_fromUtf8("label_startindex"))
        self.value_startindex = QtGui.QLabel(self.centralwidget)
        self.value_startindex.setGeometry(QtCore.QRect(751, 530, 171, 21))
        self.value_startindex.setObjectName(_fromUtf8("value_startindex"))
        self.label_stopindex = QtGui.QLabel(self.centralwidget)
        self.label_stopindex.setGeometry(QtCore.QRect(440, 560, 111, 21))
        self.label_stopindex.setObjectName(_fromUtf8("label_stopindex"))
        self.value_stopindex = QtGui.QLabel(self.centralwidget)
        self.value_stopindex.setGeometry(QtCore.QRect(751, 580, 171, 21))
        self.value_stopindex.setObjectName(_fromUtf8("value_stopindex"))
        self.label_plotindexrange = QtGui.QLabel(self.centralwidget)
        self.label_plotindexrange.setGeometry(QtCore.QRect(650, 480, 181, 31))
        self.label_plotindexrange.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_plotindexrange.setObjectName(_fromUtf8("label_plotindexrange"))
        self.value_timerange = QtGui.QLabel(self.centralwidget)
        self.value_timerange.setGeometry(QtCore.QRect(50, 530, 351, 21))
        self.value_timerange.setObjectName(_fromUtf8("value_timerange"))
        self.label_avtimerange = QtGui.QLabel(self.centralwidget)
        self.label_avtimerange.setGeometry(QtCore.QRect(40, 510, 201, 21))
        self.label_avtimerange.setObjectName(_fromUtf8("label_avtimerange"))
        self.label_currenthdf = QtGui.QLabel(self.centralwidget)
        self.label_currenthdf.setGeometry(QtCore.QRect(110, 480, 241, 31))
        self.label_currenthdf.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_currenthdf.setObjectName(_fromUtf8("label_currenthdf"))
        self.label_avindexrange = QtGui.QLabel(self.centralwidget)
        self.label_avindexrange.setGeometry(QtCore.QRect(40, 560, 201, 21))
        self.label_avindexrange.setObjectName(_fromUtf8("label_avindexrange"))
        self.value_indexrange = QtGui.QLabel(self.centralwidget)
        self.value_indexrange.setGeometry(QtCore.QRect(50, 580, 351, 21))
        self.value_indexrange.setObjectName(_fromUtf8("value_indexrange"))
        self.bg_hdftree = QtGui.QLabel(self.centralwidget)
        self.bg_hdftree.setGeometry(QtCore.QRect(20, 50, 251, 421))
        self.bg_hdftree.setText(_fromUtf8(""))
        self.bg_hdftree.setObjectName(_fromUtf8("bg_hdftree"))
        self.list = QtGui.QTreeWidget(self.centralwidget)
        self.list.setEnabled(True)
        self.list.setGeometry(QtCore.QRect(30, 60, 231, 381))
        self.list.setFrameShape(QtGui.QFrame.NoFrame)
        self.list.setFrameShadow(QtGui.QFrame.Plain)
        self.list.setLineWidth(0)
        self.list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list.setObjectName(_fromUtf8("list"))
        self.list.header().setVisible(False)
        self.list.header().setDefaultSectionSize(240)
        self.list.header().setStretchLastSection(False)
        self.btn_openfile = QtGui.QPushButton(self.centralwidget)
        self.btn_openfile.setGeometry(QtCore.QRect(30, 440, 91, 21))
        self.btn_openfile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_openfile.setFlat(True)
        self.btn_openfile.setObjectName(_fromUtf8("btn_openfile"))
        self.slider_start = QtGui.QSlider(self.centralwidget)
        self.slider_start.setGeometry(QtCore.QRect(450, 530, 281, 20))
        self.slider_start.setOrientation(QtCore.Qt.Horizontal)
        self.slider_start.setObjectName(_fromUtf8("slider_start"))
        self.slider_stop = QtGui.QSlider(self.centralwidget)
        self.slider_stop.setGeometry(QtCore.QRect(450, 580, 281, 20))
        self.slider_stop.setOrientation(QtCore.Qt.Horizontal)
        self.slider_stop.setObjectName(_fromUtf8("slider_stop"))
        self.value_progress = QtGui.QProgressBar(self.centralwidget)
        self.value_progress.setGeometry(QtCore.QRect(137, 440, 121, 23))
        self.value_progress.setProperty("value", 0)
        self.value_progress.setTextVisible(True)
        self.value_progress.setObjectName(_fromUtf8("value_progress"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HDF QuickPlot", None))
        self.checkbox_separate.setText(_translate("MainWindow", "Separate Plots", None))
        self.btn_reset.setText(_translate("MainWindow", "Reset", None))
        self.checkbox_3d.setText(_translate("MainWindow", "3D Plot", None))
        self.btn_plot.setText(_translate("MainWindow", "Plot", None))
        self.label_programtitle.setText(_translate("MainWindow", "HDF QUICKPLOT", None))
        self.btn_minimize.setText(_translate("MainWindow", "MINIMIZE", None))
        self.btn_exit.setText(_translate("MainWindow", "EXIT", None))
        self.label_startindex.setText(_translate("MainWindow", "START INDEX:", None))
        self.value_startindex.setText(_translate("MainWindow", "---", None))
        self.label_stopindex.setText(_translate("MainWindow", "STOP INDEX:", None))
        self.value_stopindex.setText(_translate("MainWindow", "---", None))
        self.label_plotindexrange.setText(_translate("MainWindow", "PLOT INDEX RANGE", None))
        self.value_timerange.setText(_translate("MainWindow", "---", None))
        self.label_avtimerange.setText(_translate("MainWindow", "AVAILABLE TIME RANGE:", None))
        self.label_currenthdf.setText(_translate("MainWindow", "CURRENT HDF STATISTICS", None))
        self.label_avindexrange.setText(_translate("MainWindow", "AVAILABLE INDEX RANGE:", None))
        self.value_indexrange.setText(_translate("MainWindow", "---", None))
        self.list.headerItem().setText(0, _translate("MainWindow", "DATA", None))
        self.btn_openfile.setText(_translate("MainWindow", "...open file(s)", None))

from lib.matplotlibwidget import MatplotlibWidget
