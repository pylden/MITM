from module.protocol.network.message import Message


class CheckIntegrityMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8606
        self.data = {"type": "Vector.<int>", "value": ""}
