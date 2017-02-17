from qtpy.QtWidgets import QWidget, QCheckBox, QToolButton, QLabel, QHBoxLayout


class DataListItem(QWidget):
    def __init__(self, *args, **kwargs):
        super(DataListItem, self).__init__(*args, **kwargs)

        # Define layout
        self._layout = QHBoxLayout(self)
        self.setLayout(self._layout)

        # Create internal widgets
        self._checkbox_widget = QCheckBox(self)
        self._tool_button_widget = QToolButton(self)
        self._label_widget = QLabel(self)

        # Add widgets to layout
        self._layout.addWidget(self._checkbox_widget)
        self._layout.addWidget(self._label_widget)
        self._layout.addWidget(self._tool_button_widget)

        # Add some generic text as the label
        self._label_widget.setText("Generic Data Text")