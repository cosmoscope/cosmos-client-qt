import six
import zerorpc
import logging

from qtpy.QtWidgets import QApplication

from .singletons import Singleton
from .models.model import DataListModel


class App(QApplication):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)


@six.add_metaclass(Singleton)
class Client:
    def __init__(self, address="127.0.0.1:4242"):
        self._api = zerorpc.Client()
        self._api.connect("tcp://{}".format(address))

    def __call__(self, name, async=True, *args, **kwargs):
        kwargs.update({'async': async})

        if hasattr(self._api, name):
            result = getattr(self._api, name)(*args, **kwargs)

            return result

        logging.error("Server has no function {}.".format(name))