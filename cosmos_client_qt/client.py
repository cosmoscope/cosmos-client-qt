import six
import zerorpc
import logging
import gevent

from .singletons import Singleton


@six.add_metaclass(Singleton)
class Client:
    def __init__(self, address="tcp://localhost:4242"):
        # Setup pusher
        self.pusher = zerorpc.Pusher()
        self.pusher.bind(address)

        # Setup subscriber
        service1 = Subscriber()
        subscriber1 = zerorpc.Subscriber(service1)
        subscriber1.connect(endpoint)
        gevent.spawn(subscriber1.run)

    def __call__(self, name, async=True, *args, **kwargs):
        kwargs.update({'async': async})

        if hasattr(self.pusher, name):
            result = getattr(self.pusher, name)(*args, **kwargs)

            return result

        logging.error("Server has no function {}.".format(name))