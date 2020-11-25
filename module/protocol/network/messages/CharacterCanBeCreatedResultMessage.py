from module.protocol.network.message import Message


class CharacterCanBeCreatedResultMessage(Message):
    def __init__(self):
        self.id = 9514
