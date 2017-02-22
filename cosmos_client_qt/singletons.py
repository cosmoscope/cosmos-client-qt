


class Singleton(type):
    def __init__(cls, name, bases, members):
        super(Singleton, cls).__init__(name, bases, members)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)

        return cls.instance