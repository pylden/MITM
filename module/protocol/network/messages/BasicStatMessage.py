from module.protocol.network.message import Message


class BasicStatMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9271
        self.timeSpent = {"type": "Number", "value": ""}
        self.statId = {"type": "uint", "value": ""}
