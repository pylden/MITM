from module.protocol.network.message import Message


class StorageObjectsRemoveMessage(Message):
    def __init__(self):
        self.id = 5584
