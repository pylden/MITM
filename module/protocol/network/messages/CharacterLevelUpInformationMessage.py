from module.protocol.network.message import Message


class CharacterLevelUpInformationMessage(Message):
    def __init__(self):
        self.id = 1775
        self.name = {"type": "String", "value": ""}
