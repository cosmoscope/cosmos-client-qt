import plotly
from plotly.graph_objs import Scatter, Layout, XAxis, YAxis, Data, Figure
import numpy as np

import uuid
import os


class WebPlot:
    def __init__(self):
        self._id = str(uuid.uuid4())

        self._data = Data([Scatter(x=np.arange(10),
                                   y=np.random.sample(10))])

        self._layout =  Layout(xaxis=XAxis(title='Life Expectancy'),
                               yaxis=YAxis(title='GDP per Capita'),
                               autosize=True, width=500, height=500)

        self._fig = Figure(data=self._data, layout=self._layout)

        self._div = plotly.offline.plot(self._fig, auto_open=False,
                                        output_type='div',
                                        include_plotlyjs=False,
                                        show_link=False,
                                        filename=self._id)

        print(self._div)

        self.set_data(False)

    def set_data(self, data, type="scatter"):
        self._data = Data([Scatter(x=np.arange(10),
                                   y=np.random.sample(10))])
        plotly.offline.plot(self._fig, auto_open=False,
                            output_type='div',
                            include_plotlyjs=False,
                            show_link=False,
                            filename=self._id)

    def html(self):
        with open(os.path.join(os.path.dirname(__file__), "template.html")) as f:
            html = f.read()

        html = html.replace("{{ plotly }}", self._div)

        return html