import os
import sys

from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from qtpy.uic import loadUi

from cosmos_client_qt.models.model import DataListModel
from cosmos_client_qt.viewers.plotly.web_plot import WebPlot

from cosmos_client_qt.widgets import resource


class App(QApplication):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = loadUi(os.path.join(os.path.dirname(__file__), "cosmos_client_qt", "ui", "main_window.ui"))
    p = loadUi(os.path.join(os.path.dirname(__file__), "cosmos_client_qt", "viewers", "plotly", "web_plot.ui"))

    m = DataListModel()

    w.data_view.setModel(m)

    w.plot_tab_area.clear()
    w.plot_tab_area.addTab(p, "Plot")

    pd = WebPlot()
    p.web_engine_view.setHtml(pd.html())

    w.setWindowTitle('Cosmoscope')
    w.show()

    sys.exit(app.exec_())