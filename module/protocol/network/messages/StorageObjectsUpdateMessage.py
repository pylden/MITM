from module.protocol.network.message import Message


class StorageObjectsUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5590
        self.objectList = {"type": "Vector.<ObjectItem>", "value": ""}
