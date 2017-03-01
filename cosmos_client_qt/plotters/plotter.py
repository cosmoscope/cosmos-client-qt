from qtpy.uic import loadUiType, loadUi
import os
import six, abc
from sip import wrappertype


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
    @abc.abstractmethod
    def add_data(self):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_data(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update_data(self):
        raise NotImplementedError