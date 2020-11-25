from module.protocol.network.message import Message


class NicknameChoiceRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5126
        self.nickname = {"type": "String", "value": ""}
