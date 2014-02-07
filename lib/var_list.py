from os import getcwd

class varList():
	# Current working directory
	CWD = getcwd()

	# Epoch offset obtained from http://www.epochconverter.com/epoch/timestamp-list.php
	# 1996, January 1: 820454400
	EPOCH_OFFSET = 820454400

	# Global values used for setting window width and height
	WINDOW_WIDTH = 1041
	WINDOW_HEIGHT = 661

	# ------
	# matplotlib.figure - "The figure module provides the top-level Artist, the Figure, which contains all the plot elements."
	# ------
	# figsize - w,h tuple in inches
	FIGURE_SIZE = (4,3)
	# dpi - dots per inch
	FIGURE_DPI = 100
	# hold - set the hold state
	FIGURE_HOLD = False
	# facecolor - the figure patch facecolor (widget background)
	FIGURE_FACECOLOR = '#444444'
	# edgecolor - the figure patch edge color (plot frame color)
	FIGURE_EDGECOLOR = '#FFFFFF'
	# linewidth - the figure patch edge linewidth (widget frame width)
	FIGURE_LINEWIDTH = 0
	# frameon - if False, suppress drawing the figure frame
	FIGURE_FRAMEON = True

	# axisbg - the background color for the axis (the plot background), default is white
	AXIS_BGCOLOR = '#FFFFFF'
	# frame_on - set whether the axes rectangle patch is drawn, accepts: [ True | False ], figure facecolor will overlap axis bg color if set to 'False'
	AXIS_FRAMEON = True

	XAXIS_LABELCOLOR = '#FFFFFF'
	XAXIS_TICKPARAMCOLOR = '#FFFFFF'
	YAXIS_LABELCOLOR = '#FFFFFF'
	YAXIS_TICKPARAMCOLOR = '#FFFFFF'
