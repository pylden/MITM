from module.protocol.network.message import Message


class EmoteListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7532
        self.emoteIds = {"type": "Vector.<uint>", "value": ""}
