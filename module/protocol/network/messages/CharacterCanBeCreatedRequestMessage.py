from module.protocol.network.message import Message


class CharacterCanBeCreatedRequestMessage(Message):
    def __init__(self):
        self.id = 2712
