from django.apps import AppConfig

from bokeh.server.server import Server

from tornado.ioloop import IOLoop

from .dashboard import LayoutDashBoard

from .utils import port

import datetime


from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer(url="https://api.ecmwf.int/v1",key="9d3f4e563ad01ca60184f9792c842476",email="ialmeida.uerj@gmail.com")

class Data:
	def __init__(self, filename, date, num):
		self.filename = filename
		
		base = datetime.datetime.today()

		date_list = [date - datetime.timedelta(days=x) for x in range(num)]

		self.date = list(map(lambda x: str(x).split()[0].replace("-", ""), date_list))
	
	def execute(self):
		print('retrieve ...')

		print("/".join(self.date[::-1]))

		server.retrieve({
		    "class": "ei",
		    "dataset": "interim",
		    "date": "20120201/20120229",
		    "expver": "1",
		    "grid": "0.75/0.75",
		    "levtype": "sfc",
		    "param": "167.128",
		    "step": "0",
		    "stream": "oper",
		    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
		    "type": "an",
			'format'    : "netcdf",
		    "target": "static/data/output.nc",
		})


def bk_worker():
	gvplot = LayoutDashBoard(filename="data.nc")
	app = gvplot.app
	server = Server({'/gmap': app},
		io_loop=IOLoop(),
		address="68.183.134.114",
		port=port,
		allow_websocket_origin=["*"])
	server.start()
	server.io_loop.start()

def ecmwf_worker():
	Data(filename="data.nc", date=datetime.datetime.today(), num=20).execute()

class CoreConfig(AppConfig):
    name = 'apps.core'
    def ready(self):
    	from threading import Thread
    	Thread(target=bk_worker).start()
    	#Thread(target=ecmwf_worker).start()