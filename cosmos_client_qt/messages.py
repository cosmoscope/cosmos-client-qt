from pivot.message import Message
from pivot.hub import Hub
import six

from .singletons import Singleton


@six.add_metaclass(Singleton)
class CentralHub(Hub):
    pass

class AddDataMessage(Message):
    pass

class LoadDataMessage(Message):
    pass

