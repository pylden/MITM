from module.protocol.network.message import Message


class ProtocolRequired(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5481
        self.version = {"type": "String", "value": ""}
