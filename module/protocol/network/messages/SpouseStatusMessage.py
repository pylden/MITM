from module.protocol.network.message import Message


class SpouseStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6318
        self.hasSpouse = {"type": "Boolean", "value": ""}
