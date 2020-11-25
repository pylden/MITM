from module.protocol.network.message import Message


class CharacterLevelUpMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 366
        self.newLevel = {"type": "uint", "value": ""}
