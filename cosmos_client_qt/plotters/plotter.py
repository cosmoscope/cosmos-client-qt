from qtpy.uic import loadUiType, loadUi
import os
import six, abc
from sip import wrappertype
from ..models.model import DataListModel

from ..hub import *


_PlotTabUI, _PlotTabBase = loadUiType(
    os.path.join(os.path.dirname(__file__), "plot_tab.ui"))


class _PlotterProxy(_PlotTabBase, _PlotTabUI):
    def __init__(self, *args, **kwargs):
        super(_PlotterProxy, self).__init__(*args, **kwargs)
        self.setupUi(self)


class _PlotterMetaProxy(abc.ABCMeta, wrappertype):
    pass


@six.add_metaclass(_PlotterMetaProxy)
class Plotter(_PlotterProxy):
    def __init__(self, *args, **kwargs):
        super(Plotter, self).__init__(*args, **kwargs)
        # Initialize model
        self._data_list_model = DataListModel()

    @property
    def data_model(self):
        return self._data_list_model

    @abc.abstractmethod
    def add_data(self, *args, **kwargs):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_data(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update_data(self):
        raise NotImplementedError