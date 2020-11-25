from module.protocol.network.message import Message


class CharacterLevelUpInformationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1775
        self.name = {"type": "String", "value": ""}
        self.id = {"type": "Number", "value": ""}
