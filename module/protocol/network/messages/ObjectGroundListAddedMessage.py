from module.protocol.network.message import Message


class ObjectGroundListAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1696
        self.cells = {"type": "Vector.<uint>", "value": ""}
        self.referenceIds = {"type": "Vector.<uint>", "value": ""}
