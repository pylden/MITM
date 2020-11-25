from module.protocol.network.message import Message


class ObjectDeleteMessage(Message):
    def __init__(self):
        self.id = 3368
