from qtpy.QtWidgets import QScrollArea, QVBoxLayout


class DataList(QScrollArea):
    def __init__(self, *args, **kwargs):
        super(DataList, self).__init__(*args, **kwargs)

        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

    def add_widget(self, widget):
        self._layout.addWidget(widget)