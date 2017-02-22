import plotly
from plotly.graph_objs import Scatter, Layout, XAxis, YAxis
import numpy as np

import uuid
import os


class WebPlot:
    def __init__(self):
        self._id = str(uuid.uuid4())

        self._div = plotly.offline.plot(
            {
                "data": [Scatter(x=np.arange(10000), y=np.random.sample(10000))],
                "layout": Layout(xaxis=XAxis(title='Life Expectancy'), yaxis=YAxis(title='GDP per Capita'),
                                 autosize=True, width=500, height=500,)
            },
            filename="{}.html".format(self._id), auto_open=False, output_type='div',
            include_plotlyjs=False, show_link=False)

        print(self._div)

    def html(self):
        with open(os.path.join(os.path.dirname(__file__), "template.html")) as f:
            html = f.read()

        html = html.replace("{{ plotly }}", self._div)

        return html