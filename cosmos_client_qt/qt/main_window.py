from qtpy.QtWidgets import QMainWindow, QDockWidget, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSplitter
from qtpy.QtCore import Qt

from .data_list import DataList
from .data_list_item import DataListItem
from .data_view import DataView
from .data_view_item import DataViewItem
from ..viewers.py_qt_graph_viewer import PyQtGraphDataViewItem

import numpy as np


class MainWindow(QMainWindow):
    """
    Main application window.
    """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create a dummy central widget
        central_widget = QWidget()
        central_layout = QHBoxLayout()
        central_widget.setLayout(central_layout)

        # The two main widgets will be separated by a splitter
        central_splitter = QSplitter()
        self.setCentralWidget(central_splitter)

        # Create the main widgets
        data_list_widget = DataList()
        data_view_widget = DataView()

        central_splitter.addWidget(data_list_widget)
        central_splitter.addWidget(data_view_widget)

        # Create test item
        test_item = DataListItem()
        test_item2 = DataListItem()
        test_item3 = DataListItem()
        data_list_widget.add_widget(test_item)
        data_list_widget.add_widget(test_item2)
        data_list_widget.add_widget(test_item3)

        # Some test views
        data_view_item = PyQtGraphDataViewItem()

        class TestData:
            def __init__(self):
                self.data = np.random.sample(100)
                self.dispersion = np.arange(100)

        data_view_item.add_data(TestData())
        data_view_widget.add_view(data_view_item)