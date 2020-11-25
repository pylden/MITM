from module.protocol.network.message import Message


class ObjectsDeletedMessage(Message):
    def __init__(self):
        self.id = 5628
