from module.protocol.network.message import Message


class EmoteAddMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7616
        self.emoteId = {"type": "uint", "value": ""}
