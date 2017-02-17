from qtpy.QtWidgets import QDockWidget

import abc
import six


class DataViewItemProxy(QDockWidget):
    def __init__(self, *args, **kwargs):
        super(DataViewItemProxy, self).__init__(*args, **kwargs)


@six.add_metaclass(abc.ABCMeta)
class DataViewItem(DataViewItemProxy):
    def __init__(self, title, data=None, *args, **kwargs):
        super(DataViewItem, self).__init__(*args, **kwargs)

    @abc.abstractmethod
    def add_data(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def update_data(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_data(self, data):
        raise NotImplementedError