from module.protocol.network.message import Message


class ObjectGroundListAddedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1696
        self.cells = {"type": "Vector.<uint>", "value": ""}
        self.referenceIds = {"type": "Vector.<uint>", "value": ""}
