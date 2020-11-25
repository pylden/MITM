from module.protocol.network.message import Message


class EmoteAddMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7616
        self.emoteId = {"type": "uint", "value": ""}
