from module.protocol.network.message import Message


class ObjectGroundRemovedMultipleMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3658
        self.cells = {"type": "Vector.<uint>", "value": ""}
