from module.protocol.network.message import Message


class CharacterLevelUpMessage(Message):
    def __init__(self):
        self.id = 366
