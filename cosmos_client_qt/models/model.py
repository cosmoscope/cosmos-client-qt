from qtpy.QtCore import Qt
from qtpy.QtCore import QAbstractListModel, QVariant, QModelIndex, QSize

import qtawesome as qta

from ..singletons import Singleton
import six
from sip import wrappertype

from ..hub import *


class DataListModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(DataListModel, self).__init__(*args, **kwargs)

        self._data = []

        # Subscribe to hub messages
        self._hub = Hub()
        self._hub.subscribe(AddDataMessage, self.setData, self)

    def add_data(self, data, row=None, parent=QModelIndex()):
        self.beginInsertRows(parent, row or self.rowCount(), 1)

        self._data.append(data)

        self.endInsertRows()

    def removeRow(self, p_int, parent=QModelIndex(), *args, **kwargs):
        self.beginRemoveRows(parent, p_int, p_int)

        self._data.pop(p_int)

        self.endRemoveRows()

    def removeRows(self, p_int, p_int_1, parent=QModelIndex(), *args, **kwargs):
        self.beginRemoveRows(parent, p_int, p_int_1)

        del self._data[p_int:p_int_1 + 1]

        self.endRemoveRows()

    def rowCount(self, parent=QModelIndex(), *args, **kwargs):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < self.rowCount():
            return QVariant()

        row = index.row()

        if role == Qt.DisplayRole:
            return str(self._data[row].name)
        elif role == Qt.DecorationRole:
            icon = qta.icon('fa.circle',
                            active='fa.circle-o',
                            color='blue',
                            color_active='orange')
            return icon

        return QVariant()

    def setData(self, index, value, *args, **kwargs):
        if not index.isValid():
            return False

        if not 0 <= index.row() < self.rowCount():
            self._data.append(value)
        else:
            self._data[index.row()] = value

        return True
