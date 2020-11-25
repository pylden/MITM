from module.protocol.network.message import Message


class ObjectsDeletedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5628
        self.objectUID = {"type": "Vector.<uint>", "value": ""}
