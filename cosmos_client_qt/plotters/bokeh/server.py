import numpy as np
from tornado.ioloop import IOLoop

from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider
from bokeh.plotting import figure
from bokeh.server.server import Server

io_loop = IOLoop.current()


class Test:
    def __init__(self):
        x = np.linspace(0, 10, 1000)
        y = np.log(x) * np.sin(x)

        source = ColumnDataSource(data=dict(x=x, y=y))

        plot = figure()
        plot.line('x', 'y', source=source)

        slider = Slider(start=1, end=10, value=1, step=0.1)

        def callback(attr, old, new):
            y = np.log(x) * np.sin(x*new)
            source.data = dict(x=x, y=y)

        slider.on_change('value', callback)

        bokeh_app = Application(FunctionHandler(
            lambda doc: doc.add_root(column(plot))
        ))

        bokeh_app.on_server_loaded = lambda x: print("Server loaded")
        bokeh_app.on_session_created = lambda x: print("Session created")
        bokeh_app.on_server_unloaded = lambda x: print("Server unloaded")
        bokeh_app.on_session_destroyed = lambda x: print("Session destroyed")

        server = Server({'/': bokeh_app}, io_loop=io_loop)
        server.start()
        server.run_until_shutdown()


if __name__ == '__main__':
    Test()