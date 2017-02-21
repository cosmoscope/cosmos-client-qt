import os
import sys

from qtpy.QtWidgets import QApplication #, QWidget, QVBoxLayout, QMainWindow
from qtpy.uic import loadUi
from cosmos_client_qt.ui.resource import *

from cosmos_client_qt.ui.widgets.plotly.web_plot import WebPlot


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = loadUi(os.path.join(os.path.dirname(__file__), "cosmos_client_qt", "ui", "main_window.ui"))
    p = loadUi(os.path.join(os.path.dirname(__file__), "cosmos_client_qt", "ui", "widgets", "plotly", "web_plot.ui"))

    w.plot_tab_area.addTab(p, "Plot")

    pd = WebPlot()
    p.web_engine_view.setHtml(pd.html())

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())