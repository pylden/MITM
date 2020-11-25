from module.protocol.network.message import Message


class ChatAbstractServerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1532
        self.channel = {"type": "uint", "value": ""}
        self.content = {"type": "String", "value": ""}
        self.timestamp = {"type": "uint", "value": ""}
        self.fingerprint = {"type": "String", "value": ""}
