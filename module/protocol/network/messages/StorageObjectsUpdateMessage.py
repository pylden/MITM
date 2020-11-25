from module.protocol.network.message import Message


class StorageObjectsUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5590
        self.objectList = {"type": "Vector.<ObjectItem>", "value": ""}
