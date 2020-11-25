from module.protocol.network.message import Message


class LocalizedChatSmileyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8274
        self.cellId = {"type": "uint", "value": ""}
