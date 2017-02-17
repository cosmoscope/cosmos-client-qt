from pyqtgraph import PlotWidget

import numpy as np

from ..qt.data_view_item import DataViewItem


class PyQtGraphDataViewItem(DataViewItem):
    def __init__(self, *args, **kwargs):
        super(PyQtGraphDataViewItem, self).__init__(*args, **kwargs)

        self._plots = {}
        self._plot_widget = PlotWidget()
        self._plot_item = self._plot_widget.getPlotItem()

        self.setWidget(self._plot_widget)

    def add_data(self, data):
        new_plot = self._plot_item.plot(data.dispersion, data.data)

        self._plots[data] = new_plot

    def update_data(self, data):
        plot = self._plots.get(data, None)

        if plot is not None:
            plot.setData(data.dispersion, data.data)

    def remove_data(self, data):
        plot = self._plots.get(data, None)

        if plot is not None:
            self._plot_item.removeItem(plot)
            del self._plots[plot]