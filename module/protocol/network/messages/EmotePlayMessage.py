from module.protocol.network.message import Message


class EmotePlayMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8116
        self.actorId = {"type": "Number", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
