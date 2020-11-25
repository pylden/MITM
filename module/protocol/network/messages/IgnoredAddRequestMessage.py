from module.protocol.network.message import Message


class IgnoredAddRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9784
        self.name = {"type": "String", "value": ""}
        self.session = {"type": "Boolean", "value": ""}
