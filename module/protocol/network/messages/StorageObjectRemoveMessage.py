from module.protocol.network.message import Message


class StorageObjectRemoveMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6168
        self.objectUID = {"type": "uint", "value": ""}
