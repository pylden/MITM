from module.protocol.network.message import Message


class EmotePlayRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9094
        self.emoteId = {"type": "uint", "value": ""}
