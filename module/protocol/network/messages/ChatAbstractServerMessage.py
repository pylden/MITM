from module.protocol.network.message import Message


class ChatAbstractServerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1532
        self.channel = {"type": "uint", "value": ""}
        self.content = {"type": "String", "value": ""}
        self.timestamp = {"type": "uint", "value": ""}
        self.fingerprint = {"type": "String", "value": ""}
