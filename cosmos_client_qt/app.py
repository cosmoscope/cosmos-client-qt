import os
import sys

from qtpy.QtCore import QSize
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication, QToolButton
from qtpy.uic import loadUiType, loadUi

from .models.model import DataListModel
from .plotters.bokeh.plots import BokehPlot

from .ui.cosmoscope_qt_rc import *


_MainWindowUI, _MainWindowBase = loadUiType(
    os.path.join(os.path.dirname(__file__), "ui", "main_window.ui"))


class _MainWindowProxy(_MainWindowBase, _MainWindowUI):
    def __init__(self, *args, **kwargs):
        super(_MainWindowProxy, self).__init__(*args, **kwargs)
        self.setupUi(self)


class MainWindow(_MainWindowProxy):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Initialize model
        self._data_list_model = DataListModel()

        # Connect model to view
        self.data_view.setModel(self._data_list_model)
        self.plot_tab_area.clear()

        # Connect to hub messages

        # Make corner button
        self._add_tab_button = QToolButton()
        self._add_tab_button.setFixedSize(QSize(29, 29))
        self._add_tab_button.setText("+")
        self.plot_tab_area.setCornerWidget(self._add_tab_button,
                                           Qt.TopRightCorner)

        # Set main window title
        self.setWindowTitle('Cosmoscope')

        self.plot_tab_area.addTab(BokehPlot(), "New Tab")

    def add_plot_tab(self, plotter):
        self._main_window.plot_tab_area.addTab(plotter, "Plot")


def main():
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())