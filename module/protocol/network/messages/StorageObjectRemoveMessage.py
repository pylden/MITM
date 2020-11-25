from module.protocol.network.message import Message


class StorageObjectRemoveMessage(Message):
    def __init__(self):
        self.id = 6168
