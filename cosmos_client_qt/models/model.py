from qtpy.QtCore import Qt
from qtpy.QtCore import QAbstractListModel, QVariant, QModelIndex, QSize

import qtawesome as qta

from ..singletons import Singleton
import six
from sip import wrappertype


class ModelMetaProxy(Singleton, wrappertype):
    pass


@six.add_metaclass(ModelMetaProxy)
class DataListModel(QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(DataListModel, self).__init__(*args, **kwargs)

        self._data = [70, 90, 20, 50]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or not 0 <= index.row() < self.rowCount():
            return QVariant()

        row = index.row()

        if role == Qt.DisplayRole:
            return str(self._data[row])
        elif role == Qt.DecorationRole:
            icon = qta.icon('fa.circle',
                            active='fa.circle-o',
                            color='blue',
                            color_active='orange')
            return icon

        return QVariant()

    def setData(self, index, value):
        if not index.isValid():
            return False

        if not 0 <= index.row() < self.rowCount():
            self._data.append(value)
        else:
            self._data[index.row()] = value

        return True
