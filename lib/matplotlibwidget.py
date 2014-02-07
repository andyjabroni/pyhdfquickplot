#__version__ = "1.0.0"

from PyQt4.QtGui import QSizePolicy
from PyQt4.QtCore import QSize

#aaimport matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from matplotlib import rcParams
rcParams['font.size'] = 9

# Import the variable list module
from lib.var_list import varList

class MatplotlibWidget(FigureCanvas):
	"""Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
	"""
	MatplotlibWidget inherits PyQt4.QtGui.QWidget
	and matplotlib.backend_bases.FigureCanvasBase
   
	Options: option_name (default_value)
    -------
    parent (None): parent widget
    title (''): figure title
    xlabel (''): X-axis label
    ylabel (''): Y-axis label
    xlim (None): X-axis limits ([min, max])
    ylim (None): Y-axis limits ([min, max])
    xscale ('linear'): X-axis scale
    yscale ('linear'): Y-axis scale
    width (4): width in inches
    height (3): height in inches
    dpi (100): resolution in dpi
    hold (False): if False, figure will be cleared each time plot is called
   
	Widget attributes:
	-----------------
	figure: instance of matplotlib.figure.Figure
	axes: figure axes
	"""
	def __init__(self, parent=None):
		# Read varList comments for parameter descriptions
		fig = Figure(figsize=varList.FIGURE_SIZE, dpi=varList.FIGURE_DPI, facecolor=varList.FIGURE_FACECOLOR, edgecolor=varList.FIGURE_EDGECOLOR, linewidth=varList.FIGURE_LINEWIDTH, frameon=varList.FIGURE_FRAMEON)		
		self.axes = fig.add_subplot(1,1,1, axis_bgcolor=varList.AXIS_BGCOLOR, frame_on=varList.AXIS_FRAMEON)
		self.axes.xaxis.label.set_color(varList.XAXIS_LABELCOLOR)
		self.axes.tick_params(axis='x', colors=varList.XAXIS_TICKPARAMCOLOR)		
		self.axes.yaxis.label.set_color(varList.YAXIS_LABELCOLOR)
		self.axes.tick_params(axis='y', colors=varList.XAXIS_TICKPARAMCOLOR)
		# We want the axes cleared every time plot() is called
		self.axes.hold(varList.FIGURE_HOLD)
		self.compute_initial_figure()

		FigureCanvas.__init__(self,fig)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)

	def compute_initial_figure(self):
		pass