import os
import sys
import logging

from qtpy.QtCore import QSize
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication, QToolButton
from qtpy.uic import loadUiType, loadUi

from .models.model import DataListModel
from .plotters.bokeh.plots import BokehPlot
from .client import start

from .ui.cosmoscope_qt_rc import *
from .hub import *


_MainWindowUI, _MainWindowBase = loadUiType(
    os.path.join(os.path.dirname(__file__), "ui", "main_window.ui"))


class _MainWindowProxy(_MainWindowBase, _MainWindowUI):
    def __init__(self, *args, **kwargs):
        super(_MainWindowProxy, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Clear tab area
        self.plot_tab_area.clear()

        # Make corner button
        self._add_tab_button = QToolButton()
        self._add_tab_button.setFixedSize(QSize(29, 29))
        self._add_tab_button.setText("+")
        self.plot_tab_area.setCornerWidget(self._add_tab_button,
                                           Qt.TopRightCorner)

        # Set main window title
        self.setWindowTitle('Cosmoscope')


class MainWindow(_MainWindowProxy):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Setup hub connection
        self._hub = Hub()

        # Initialize model
        self._data_list_model = DataListModel()

        # Connect model to view
        self.data_view.setModel(self._data_list_model)

        self.setup_connections()

    def setup_connections(self):
        # Connect tab opening buttons
        self._add_tab_button.pressed.connect(self.add_plot_tab)
        # self.add_plot_tab()

        # Tab closing connections
        def remove_tab(index):
            widget = self.plot_tab_area.widget(index)

            if widget is not None:
                widget.deleteLater()

            self.plot_tab_area.removeTab(index)

            if self.plot_tab_area.count() == 0:
                self.add_plot_tab()

        self.plot_tab_area.tabCloseRequested.connect(remove_tab)

    def add_plot_tab(self, name=None):
        self._hub.publish(LoadDataMessage, "/some/where/over/rainbow")

        if name is None:
            count = self.plot_tab_area.count() + 1
            name = "New Plot {}".format(count)

        self.plot_tab_area.addTab(BokehPlot(), name)


def main():
    logging.info("[client] Starting services...")

    # Start the client listeners
    start()

    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())