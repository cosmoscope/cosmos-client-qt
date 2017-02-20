from qtpy.QtWidgets import QDockWidget

import abc
import six


class DataViewItem(QDockWidget):
    def __init__(self, title, data=None, *args, **kwargs):
        super(DataViewItem, self).__init__(*args, **kwargs)

    def add_data(self, data):
        raise NotImplementedError

    def update_data(self, data):
        raise NotImplementedError

    def remove_data(self, data):
        raise NotImplementedError