import sys
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from cosmos_client_qt.qt.main_window import MainWindow

from qtpy.uic import loadUi
import os

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = MainWindow()

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())