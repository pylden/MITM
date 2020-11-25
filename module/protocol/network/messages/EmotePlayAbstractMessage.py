from module.protocol.network.message import Message


class EmotePlayAbstractMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7499
        self.emoteId = {"type": "uint", "value": ""}
        self.emoteStartTime = {"type": "Number", "value": ""}
