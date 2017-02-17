import sys
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from cosmos_client_qt.ui.widgets.docking.q_dock_area import QDockArea
from cosmos_client_qt.ui.widgets.docking.q_dock_item import QDockItem

from qtpy.uic import loadUi
import os

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = loadUi(os.path.join(os.path.dirname(__file__), 'cosmos_client_qt', 'ui', 'mainwindow.ui'))
    d = loadUi(os.path. join(os.path.dirname(__file__), 'cosmos_client_qt', 'ui', 'data_item.ui'))

    w.verticalLayout_2.addWidget(d)

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())