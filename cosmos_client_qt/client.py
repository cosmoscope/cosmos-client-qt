import zerorpc


def run():
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")

    print(c.load_data("my/path"))