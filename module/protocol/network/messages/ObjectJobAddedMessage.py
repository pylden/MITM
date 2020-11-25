from module.protocol.network.message import Message


class ObjectJobAddedMessage(Message):
    def __init__(self):
        self.id = 355
