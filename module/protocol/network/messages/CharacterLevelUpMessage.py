from module.protocol.network.message import Message


class CharacterLevelUpMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 366
        self.newLevel = {"type": "uint", "value": ""}
