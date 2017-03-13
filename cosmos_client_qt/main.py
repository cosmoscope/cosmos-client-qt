import os
import sys
import logging

from qtpy.QtCore import QSize
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QApplication, QToolButton, QFileDialog
from qtpy.uic import loadUiType, loadUi

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

        self._hub.subscribe(AddDataMessage, self.add_data, self)

        self.setup_connections()

        # Add a default new plot tab
        self.new_plot_tab()

    def setup_connections(self):
        # Connect tab opening buttons
        self._add_tab_button.pressed.connect(self.new_plot_tab)

        # Tab closing connections
        def remove_tab(index):
            widget = self.plot_tab_area.widget(index)

            if widget is not None:
                widget.deleteLater()

            self.plot_tab_area.removeTab(index)

            if self.plot_tab_area.count() == 0:
                self.new_plot_tab()

        self.plot_tab_area.tabCloseRequested.connect(remove_tab)

        # On tab selection, switch out the data model used for the list view
        self.plot_tab_area.currentChanged.connect(self._set_data_model)

        # Open data file action
        self.action_open.triggered.connect(self.file_open)

    def _set_data_model(self, index):
        widget = self.plot_tab_area.widget(index)
        print("Changing model")

        if widget is not None:
            self.data_view.setModel(widget.data_model)

    def file_open(self):
        file_name, selected_filter = QFileDialog.getOpenFileName()

        self._hub.publish(LoadDataMessage, file_name, selected_filter)

    def new_plot_tab(self, name=None):
        if name is None:
            count = self.plot_tab_area.count() + 1
            name = "New Plot {}".format(count)

        new_plot = BokehPlot()
        self.plot_tab_area.addTab(new_plot, name)
        self.plot_tab_area.setCurrentWidget(new_plot)
        self.plot_tab_area.currentWidget().add_data()

    def add_data(self, data):
        print("Adding data", data.name)

        # Get current tab plot
        self.plot_tab_area.currentWidget().data_model.add_data(data)
        self.plot_tab_area.currentWidget().add_data(data)


def main():
    logging.info("[client] Starting services...")

    # Start the client listeners
    start()

    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings, True)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())