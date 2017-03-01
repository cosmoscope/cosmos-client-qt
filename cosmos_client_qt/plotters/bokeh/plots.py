import os
from tornado.ioloop import IOLoop

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.server.server import Server
from bokeh.embed import autoload_server

from qtpy.QtCore import QUrl, QEventLoop, QThread

import numpy as np
import threading
from itertools import cycle

from ..plotter import Plotter

io_loop = IOLoop.current()

ports = cycle(range(5006, 5106))


class LoopThread(QThread):
    def __init__(self, loop, *args, **kwargs):
        super(LoopThread, self).__init__(*args, **kwargs)
        self._loop = loop

    def run(self):
        self._loop.start()

    def stop(self):
        self._loop.stop(True)


server_thread = LoopThread(io_loop)
server_thread.start()


class BokehPlot(Plotter):
    def __init__(self, *args, **kwargs):
        super(BokehPlot, self).__init__(*args, **kwargs)

        self._fig = figure(sizing_mode='scale_width')

        x = np.linspace(0, 10, 1000)
        y = np.log(x) * np.sin(x)

        source = ColumnDataSource(data=dict(x=x, y=y))

        self._fig.line('x', 'y', source=source)

        app = Application(FunctionHandler(
            lambda doc: doc.add_root(column(self._fig))))

        app.on_server_loaded = lambda x: print("Server loaded")
        app.on_session_created = lambda x: print("Session created")
        app.on_server_unloaded = lambda x: print("Server unloaded")
        app.on_session_destroyed = lambda x: print("Session destroyed")

        self._server = Server({'/': app}, io_loop=io_loop, port=next(ports))
        self._server.start()

        self.web_engine_view.setUrl(QUrl("http://localhost:{}/".format(
            self._server.port)))

    def add_data(self):
        x = np.linspace(0, 10, 1000)
        y = np.log(x) * np.sin(x)

        source = ColumnDataSource(data=dict(x=x, y=y))

        self._fit.plot('x', 'y', source=source)

    def remove_data(self):
        pass

    def update_data(self):
        pass