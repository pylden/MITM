from module.protocol.network.messages.CharacterLevelUpMessage import CharacterLevelUpMessage


class CharacterLevelUpInformationMessage(CharacterLevelUpMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CharacterLevelUpMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1775
        self.name = {"type": "String", "value": ""}
        self.id = {"type": "Number", "value": ""}
