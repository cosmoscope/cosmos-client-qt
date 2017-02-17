from qtpy.QtWidgets import QMainWindow
from qtpy.QtCore import Qt


class DataView(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(DataView, self).__init__(*args, **kwargs)


    def add_view(self, widget):
        self.addDockWidget(Qt.RightDockWidgetArea, widget)