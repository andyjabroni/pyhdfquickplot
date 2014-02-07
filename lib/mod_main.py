# Import Qt modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np
import time
from datetime import datetime
from os import system, remove
from shutil import copy2, move

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import dates

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

import h5py
import re
import ftplib

# Import the compiled UI module
from ui.ui_main import Ui_MainWindow
# Import the variable list module
from var_list import varList

class MainUI(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowFlags(Qt.FramelessWindowHint)

		QObject.connect(self.ui.btn_minimize, SIGNAL('clicked()'), self.minimizeWindow)
		QObject.connect(self.ui.btn_exit, SIGNAL('clicked()'), self.closeEvent)

		QObject.connect(self.ui.btn_openfile, SIGNAL('clicked()'), self.openFile)

		QObject.connect(self.ui.btn_reset, SIGNAL('clicked()'), self.clearPlot)
		QObject.connect(self.ui.btn_plot, SIGNAL('clicked()'), self.onDraw)
		
		QObject.connect(self.ui.lineedit_startindex, SIGNAL('textChanged(QString)'), self.timeUpdate)
		QObject.connect(self.ui.lineedit_stopindex, SIGNAL('textChanged(QString)'), self.timeUpdate)

		QObject.connect(self.ui.checkbox_separate, SIGNAL('toggled(bool)'), self.separatePlots)
		QObject.connect(self.ui.checkbox_3d, SIGNAL('toggled(bool)'), self.plot3d)

		box = self.ui.mplwidget.axes.get_position()
		self.ui.mplwidget.axes.set_position([box.x0 * 0.5, box.y0 + box.height * 0.125, box.width * 1.15, box.height * 0.9])

		tempftp = ftplib.FTP('mussel.srl.caltech.edu')
		tempftp.login('anonymous', 'anonymous')
		tempftpdir = '/pub/ace/level2/'
		tempftp.cwd(tempftpdir)
		hdfdirs = []
		for each in tempftp.nlst():
			if ('.' not in each) and (each != 'Changelog') and (each != 'README'):
				tempftp.cwd(tempftpdir + each)
				temphdflist = []
				for x in tempftp.nlst():
					if x.endswith('.hdf'):
						temphdflist.append(x)
						if x.split('.')[0]:
							pass
				hdfdirs.append(temphdflist)
				tempftp.cwd(tempftpdir)
		print hdfdirs
		tempftp.close()
		
	def timeUpdate(self):
		objectName = self.sender().objectName()
		tmpstring = str(self.sender().displayText())
		try:
			tmplastchar = tmpstring[len(str(self.sender().displayText()))-1]
			if tmplastchar.isdigit():
				self.sender().setText(tmpstring)
				tmptimeindex = int(self.sender().displayText())
				tmptime = time.gmtime((self.dataSet[tmptimeindex][7]+varList.EPOCH_OFFSET))
				tmptimestring = time.strftime("%Y/%m/%d %H:%M:%S", tmptime)
				if objectName == 'lineedit_startindex':				
					self.ui.value_startindex.setText(tmptimestring)
					self.timeStartIndex = int(self.ui.lineedit_startindex.displayText())
					self.ui.slider_start.setValue(int(tmpstring))
				elif objectName == 'lineedit_stopindex':
					self.ui.value_stopindex.setText(tmptimestring)
					self.timeStopIndex = int(self.ui.lineedit_stopindex.displayText())
					self.ui.slider_stop.setValue(int(tmpstring))
			else:
				self.sender().setText(tmpstring[:-1])
				if objectName == 'slider_start':				
					self.ui.slider_start.setValue(int(tmpstring[:-1]))
				elif objectName == 'slider_stop':
					self.ui.slider_stop.setValue(int(tmpstring[:-1]))
		except:
			if objectName == 'lineedit_startindex':				
				self.ui.value_startindex.setText('---')
				#if self.ui.lineedit_startindex.displayText() == '':
				#	self.ui.slider_start.setValue(0)
			elif objectName == 'lineedit_stopindex':
				self.ui.value_stopindex.setText('---')
				#if self.ui.lineedit_stopindex.displayText() == '':
				#	self.ui.slider_stop.setValue(0)

	def sliderHandler(self, event):
		objectName = self.sender().objectName()
		if objectName == 'slider_start':
			self.ui.lineedit_startindex.setText(str(event))			
		elif objectName == 'slider_stop':
			self.ui.lineedit_stopindex.setText(str(event))
		if int(self.ui.lineedit_startindex.displayText()) > int(self.ui.lineedit_stopindex.displayText()):
			self.ui.value_startindex.setStyleSheet('color:red;')
			self.ui.value_stopindex.setStyleSheet('color:red;')
			self.ui.lineedit_startindex.setStyleSheet('color:red;')
			self.ui.lineedit_stopindex.setStyleSheet('color:red;')
		else:
			self.ui.value_startindex.setStyleSheet('color:white;')
			self.ui.value_stopindex.setStyleSheet('color:white;')
			self.ui.lineedit_startindex.setStyleSheet('color:black;')
			self.ui.lineedit_stopindex.setStyleSheet('color:black;')

	def mouseMoveEvent(self, event):
		try:
			self.setGeometry(QRect(event.globalX() - self.offset.x(), event.globalY() - self.offset.y(), varList.WINDOW_WIDTH, varList.WINDOW_HEIGHT))
		except:
			pass

	def mousePressEvent(self, event):
		self.offset = event.pos()

	def minimizeWindow(self):
		self.showMinimized()

	def closeEvent(self):
		try:
			remove(varList.CWD + '\\tempHDF.hdf4')
			remove(varList.CWD + '\\tempHDF.hdf5')
			#remove(varList.CWD + '\\hdfbrowserlib\\temp\\tempHDF.hdf4')
			#remove(varList.CWD + '\\hdfbrowserlib\\temp\\tempHDF.hdf5')
		except:
			pass
		self.deleteLater()

	def openFile(self):
		self.filename = str(QFileDialog.getOpenFileName(self, 'Open File', '.'))

		try:
			self.db = h5py.File(self.filename,'r')
		except IOError:
			copy2(self.filename,'tempHDF.hdf4')
			cmdline = 'h4toh5convert-win32.exe ' + 'tempHDF.hdf4' + ' ' + 'tempHDF.hdf5'
			system(cmdline)
			self.db = h5py.File('tempHDF.hdf5','r')

		# Insert groups/top level dir into the list..
		for each in self.db:		
			if '_data_' in str(each):	
			#if not str(each).endswith('_doy'):
				tmpdataset = self.db[str(each)]
				for a in tmpdataset:
					if not str(a).endswith('_t'):
						self.dataSet = tmpdataset[str(a)]
				columnHeaders = []
				for b in self.dataSet.attrs.iteritems():
					if str(b[0]).startswith('FIELD_'):
						columnHeaders.append(b[1])

				tmpitem = QTreeWidgetItem([each])
				tmpcnt = -1				
				for c in columnHeaders:
					tmpcnt = tmpcnt + 1
					tmpchild = QTreeWidgetItem([c])
					tmpchild.setCheckState(0, Qt.Unchecked)
					tmpchild.number = tmpcnt
					tmpitem.addChild(tmpchild)
				self.ui.list.addTopLevelItem(tmpitem)
				self.ui.list.expandItem(tmpitem)		
		
		self.dataLength = self.dataSet.len()
		self.dataSet = np.array(self.dataSet)
		self.db.close()
		#move(varList.CWD + '\\tempHDF.hdf4', varList.CWD + '\\hdfbrowserlib\\temp\\tempHDF.hdf4')
		#move(varList.CWD + '\\tempHDF.hdf5', varList.CWD + '\\hdfbrowserlib\\temp\\tempHDF.hdf5')

		self.epochIndex = columnHeaders.index('ACEepoch')
		tmpepochstart = time.gmtime((self.dataSet[0][self.epochIndex]+varList.EPOCH_OFFSET))
		tmpepochstop = time.gmtime((self.dataSet[self.dataLength-1][self.epochIndex]+varList.EPOCH_OFFSET))
		tmpstart = time.strftime("%Y/%m/%d %H:%M:%S",tmpepochstart)
		tmpstop = time.strftime("%Y/%m/%d %H:%M:%S",tmpepochstop)
		tmptimerange = "%s - %s" %(tmpstart,tmpstop)
		self.ui.value_timerange.setText(tmptimerange)

		tmpindexrange = "0 - %i" %(self.dataLength-1)
		self.ui.value_indexrange.setText(tmpindexrange)

		self.ui.slider_start.setMaximum(self.dataLength-1)
		self.ui.slider_start.setTickInterval(1)
		self.ui.slider_start.setValue(0)
		self.ui.lineedit_startindex.setText(str(0))		
		self.connect(self.ui.slider_start, SIGNAL("valueChanged(int)"), self.sliderHandler)
		self.timeStartIndex = 0
		self.ui.slider_stop.setMaximum(self.dataLength-1)
		self.ui.slider_stop.setTickInterval(1)
		self.ui.slider_stop.setValue(self.dataLength-1)
		self.ui.lineedit_stopindex.setText(str(self.dataLength-1))
		self.connect(self.ui.slider_stop, SIGNAL("valueChanged(int)"), self.sliderHandler)
		self.timeStopIndex = self.dataLength-1	

	def checkHandler(self):
		if self.sender().checkState():
			print "checkmark test"

	def onDraw(self):
		try:
			if (self.timeStartIndex and self.timeStopIndex):
				pass
		except:
			QMessageBox.information(self, 'File Error', 'Please open an HDF file before proceeding.', QMessageBox.Ok)
			return
		self.ui.value_progress.setRange(0,0)

		# Find checked objects
		root = self.ui.list.invisibleRootItem()
		child_count = root.childCount()
		if child_count == 1:
			newroot = root.child(0)
			childrenitems = newroot.takeChildren()
			tmpchecked = []
			for each in childrenitems:
				if each.checkState(0):
					tmpchecked.append(each.number)
			newroot.addChildren(childrenitems)

		if (self.timeStartIndex < self.timeStopIndex):
			if (len(tmpchecked) > 0):
				beginPlotTimeStruct = time.gmtime((self.dataSet[self.timeStartIndex][self.epochIndex]+varList.EPOCH_OFFSET))
				stopPlotTimeStruct = time.gmtime((self.dataSet[self.timeStopIndex][self.epochIndex]+varList.EPOCH_OFFSET))
				beginPlotTimeString = time.strftime("%Y/%m/%d %H:%M:%S", beginPlotTimeStruct)
				stopPlotTimeString = time.strftime("%Y/%m/%d %H:%M:%S", stopPlotTimeStruct)
				plotTimeRangeTitle = "%s - %s" %(beginPlotTimeString, stopPlotTimeString)

				timeLabels = []
				for x in range(self.timeStartIndex, self.timeStopIndex+1):			
					tmpepoch = self.dataSet[x][self.epochIndex]+varList.EPOCH_OFFSET
					timeLabels.append(tmpepoch)
				dts = map(datetime.fromtimestamp, timeLabels)
				timeLabels = dates.date2num(dts) # converted		
		
				tmpdataslice = self.dataSet[self.timeStartIndex:self.timeStopIndex+1]
				
				tmpalldata = []		
				for each in tmpchecked:
					tmpplotdata = []			
					for x in range(0,len(tmpdataslice)):
						#print tmpdataslice[x][each]
						try:
							if str(tmpdataslice[x][each]) == '-999.9':
								tmpdataslice[x][each] = str(tmpdataslice[x][each]).replace('-999.9','NaN')
						except:
							pass
						try:
							if -999.9 in tmpdataslice[x][each]:
								if len(tmpdataslice[x][each]) > 1:
									for i in range(0,len(tmpdataslice[x][each])):
										tmpdataslice[x][each][i] = str(tmpdataslice[x][each][i]).replace('-999.9','NaN')
						except:
							pass
						tmpplotdata.append(tmpdataslice[x][each])
					#self.downsample_to_proportion(tmpplotdata,3)
					#print len(tmpplotdata)
					tmpalldata.append(tmpplotdata)


				#self.ui.mplwidget.axes.clear()
				#self.ui.mplwidget.draw()

				tmpstring = ''
				#print len(tmpalldata)
				for x in range(0,len(tmpalldata)):
					#self.ui.value_progress.setValue(x)
					tmpstring = tmpstring + 'timeLabels, tmpalldata['+str(x)+'], '
				tmpcmd_plot = tmpstring[0:len(tmpstring)-2]
				tmpexecstring = "self.ui.mplwidget.axes.plot(" + tmpcmd_plot + ")"
				exec tmpexecstring

				formatter = dates.DateFormatter('(%Y/%m/%d) %H:%M:%S')
				self.ui.mplwidget.axes.xaxis.set_major_formatter(formatter)
				self.ui.mplwidget.axes.xaxis_date()
				self.ui.mplwidget.axes.set_xlim(min(timeLabels),max(timeLabels))
				#self.ui.mplwidget.axes.set_ylim(tmpmin-tmpmax*0.1,tmpmax+tmpmax*0.1)
				plt.setp( self.ui.mplwidget.axes.get_xticklabels(),rotation='45',horizontalalignment='right',size='x-small' )
				self.ui.mplwidget.axes.set_title(plotTimeRangeTitle)
				self.ui.mplwidget.draw()
				self.ui.value_progress.setRange(0,100)
				self.ui.value_progress.setValue(100)
			else:
				QMessageBox.information(self, 'Plotting Error', 'No data items were selected, please select data to plot.', QMessageBox.Ok)
		else:
			QMessageBox.information(self, 'Index Error', 'Invalid index range, please check inputted indices.', QMessageBox.Ok)

	def downsample_to_proportion(self, values, proportion):
		print len(values)
		if (len(values) > 1000):
			#values = scipy.signal.decimate(values, int(len(values)/1)+1)
			print int(len(values)/proportion)+1

	def plot3d(self):
		# Verify that checkbox is checkmarked
		if self.ui.checkbox_3d.checkState():
			fullDataChoice = self.dataTuplet
			xCoord = list()
			yCoord = list()
			zCoord = list()

			for x in range(143000,143500):
				xCoord.append(self.dataSet[x][27])
				yCoord.append(self.dataSet[x][28])
				zCoord.append(self.dataSet[x][29])
				#print "(%i, %i, %i)" %(xCoord[x-102600], yCoord[x-102600], zCoord[x-102600])

			#print self.dataSet[102600][15]
			#print xCoord
			#print yCoord
			#print zCoord
		
			self.ui.mplwidget.axes = Axes3D(self.ui.mplwidget.figure)

			self.ui.mplwidget.axes.plot(xCoord, yCoord, zCoord)
			self.ui.mplwidget.draw()

	def separatePlots(self):
		if self.ui.checkbox_separate.checkState():
			pass

	def clearPlot(self):
		#self.ui.mplwidget.axes.clear()
		self.ui.mplwidget.axes.cla()
		self.ui.mplwidget.draw()