from module.protocol.network.message import Message


class ObjectGroundRemovedMultipleMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3658
        self.cells = {"type": "Vector.<uint>", "value": ""}
