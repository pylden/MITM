from module.protocol.network.message import Message


class StorageObjectUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1134
        self.object = {"type": "ObjectItem", "value": ""}
