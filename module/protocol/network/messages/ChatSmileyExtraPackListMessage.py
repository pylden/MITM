from module.protocol.network.message import Message


class ChatSmileyExtraPackListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2629
        self.packIds = {"type": "Vector.<uint>", "value": ""}
