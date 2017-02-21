import sys
import os

from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from qtpy.uic import loadUi

from cosmos_client_qt.ui import resource


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = loadUi(os.path.join(os.path.dirname(__file__), "cosmos_client_qt", "ui", "cosmoscope-qt.ui"))

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())