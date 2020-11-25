from module.protocol.network.message import Message


class ReloginTokenStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8519
        self.validToken = {"type": "Boolean", "value": ""}
        self.ticket = {"type": "Vector.<int>", "value": ""}
