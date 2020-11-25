from module.protocol.network.message import Message


class CharacterCreationResultMessage(Message):
    def __init__(self):
        self.id = 7140
