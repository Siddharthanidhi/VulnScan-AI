COLLECTORS = []


def register(cls):

    COLLECTORS.append(cls())

    return cls