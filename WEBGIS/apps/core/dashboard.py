import geoviews as gv
import geoviews.feature as gf
import xarray as xr
from cartopy import crs

import datetime

import os, sys

from bokeh.io import output_file, show
from bokeh.layouts import column, widgetbox
from bokeh.plotting import figure

from bokeh.models.widgets import Button, RadioButtonGroup, Select, Slider

from .utils import dataDir

gv.extension('bokeh')
import holoviews as hv

renderer = hv.renderer('bokeh')

from bokeh.resources import CDN, INLINE
from bokeh.layouts import column, row
from bokeh.embed import components

from holoviews import opts

renderer = renderer.instance(mode='server')

import cmocean

from glob import glob


cmapThermal = cmocean.cm.thermal

class Model(object):
	"""docstring for Model"""
	def __init__(self):
		super(Model, self).__init__()
		self.butons = []
	def setValues(self, args):
		for key, value in args.items():
			exec('self.%s = %r' % (key, value))

	def setButtom(self, text):
		self.butons.append(Button(label=text))

class Ensemble(Model):
 	"""docstring for Ensemble"""
 	def __init__(self, **kwargs):

 		super(Ensemble, self).__init__()

 		self.setValues(kwargs)

 		self.data = xr.open_dataset(os.path.join(dataDir, self.filename), decode_times=False, decode_cf=True ,use_cftime=True)
 		print(self.data)

 	@property
 	def dimensions(self):
 		return ['longitude', 'latitude', 'time']


class Plot:
    def execute(self): pass


class xarray(Plot):
	def __init__(self, filename):
		self.filename = filename
	def execute(self):

		ensemble = Ensemble(filename=self.filename)
		print(ensemble)
		dataset = gv.Dataset(ensemble.data, 
							ensemble.dimensions,
							'u10',
							crs=crs.PlateCarree())

		images = dataset.to(gv.Image)

		im = images.opts(cmap=cmapThermal, colorbar=True, width=600, height=500)\
			 * gf.coastline

		print( repr(im) )

		gvplot = renderer.html(im)

		hvplot = renderer.get_plot(im)
		#hvslider = renderer.get_slider(im)

		print(hvplot.state)
		#script, div = components(gvplot.roots)
		#doc = renderer.server_doc(im)

		return im



class Macro:
    def __init__(self):
        self.commands = []
    def add(self, command):
        self.commands.append(command)
    def run(self):
        for c in self.commands:
            c.execute()


class LayoutDashBoard(Model):
	def __init__(self, **kwargs):

		super(LayoutDashBoard, self).__init__()

		self.setValues(kwargs)

		gvplot = xarray(filename=self.filename).execute()

		self.plot =renderer.html(gvplot)
		self.app = renderer.app(gvplot)



	def run(self):
		self.macro.run()


