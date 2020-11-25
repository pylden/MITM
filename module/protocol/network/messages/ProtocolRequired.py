from module.protocol.network.message import Message


class ProtocolRequired(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5481
        self.version = {"type": "String", "value": ""}
