import six, abc
import logging
from collections import namedtuple

from .singletons import Singleton


Receipt = namedtuple('Receipt', ['handler', 'subscriber', 'filter'])


@six.add_metaclass(Singleton)
class Hub:
    def __init__(self):
        self._subscriptions = {}

    def subscribe(self, message, handler, subscriber, filt=lambda x, y: True):
        if isinstance(message, Message):
            logging.error("Message is not of type {}.".format(Message))
            return

        receipt = Receipt(handler, subscriber, filt)

        self._subscriptions.setdefault(message, []).append(receipt)

    def unsubscribe(self, message, subscriber):
        self._subscriptions.get(message, []).remove(subscriber)

    def publish(self, message, publisher=None, *args, **kwargs):
        print("Sending message {}".format(message))
        subs = self._subscriptions.get(message, [])
        filt_subs = [rec.handler(*args, **kwargs)
                     for rec in subs if rec.filter(message, publisher)]


@six.add_metaclass(abc.ABCMeta)
class Message:

    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError


class AddDataMessage(Message):
    pass

class LoadDataMessage(Message):
    pass

