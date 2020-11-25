from module.protocol.network.message import Message


class ObjectAddedMessage(Message):
    def __init__(self):
        self.id = 4410
