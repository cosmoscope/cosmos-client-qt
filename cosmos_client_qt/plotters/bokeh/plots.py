import os
from tornado.ioloop import IOLoop
from tornado import gen

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure, curdoc
from bokeh.server.server import Server
from bokeh.embed import autoload_server

from qtpy.QtCore import QUrl, QEventLoop, QThread

import numpy as np
import time
from itertools import cycle
from functools import partial

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

        self._doc = None
        self._fig = figure(sizing_mode='stretch_both')

        def _set_root(doc):
            self._doc = doc
            doc.add_root(column(self._fig, sizing_mode='stretch_both'))

        app = Application(FunctionHandler(_set_root))
        app.on_server_loaded = lambda x: print("[server] Bokeh server loaded")
        app.on_session_created = lambda x: print("[server] Bokeh session loaded")
        app.on_server_unloaded = lambda x: print("[server] Bokeh server unloaded")
        app.on_session_destroyed = lambda x: print("[server] Bokeh session destroyed")

        self._server = Server({'/': app}, io_loop=io_loop, port=next(ports))
        self._server.start()

        self.web_engine_view.setUrl(QUrl("http://localhost:{}/".format(
            self._server.port)))

        data = {'py{}'.format(i): [None]*100 for i in range(10)}
        data.update({'px{}'.format(i): [None]*100 for i in range(10)})

        self._source = ColumnDataSource(data=data)

        self._line_collection = [(i, self._fig.line('px{}'.format(i),
                                                'py{}'.format(i),
                                                source=self._source))
                                 for i in range(10)]

        self._data_collection = {}

    def _update_doc(self, x, y, p_ind):
        data = self._source.data
        data.update({'px{}'.format(p_ind): x})
        data.update({'py{}'.format(p_ind): y})

        self._source.data = data

    def add_data(self, data=None):
        if data is None:
            return

        p_ind, p = self._line_collection.pop(0)
        self._data_collection[data] = (p_ind, p)

        x, y = data.dispersion, data.data

        self._doc.add_next_tick_callback(partial(self._update_doc, x, y, p_ind))

    def remove_data(self):
        pass

    def update_data(self):
        pass