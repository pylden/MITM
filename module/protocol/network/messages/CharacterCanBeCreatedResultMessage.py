from module.protocol.network.message import Message


class CharacterCanBeCreatedResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9514
        self.yesYouCan = {"type": "Boolean", "value": ""}
