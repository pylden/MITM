from module.protocol.network.message import Message


class ObjectGroundRemovedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1247
        self.cell = {"type": "uint", "value": ""}
