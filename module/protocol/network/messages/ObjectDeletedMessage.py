from module.protocol.network.message import Message


class ObjectDeletedMessage(Message):
    def __init__(self):
        self.id = 5667
