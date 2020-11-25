from module.protocol.network.message import Message


class CharacterSelectedSuccessMessage(Message):
    def __init__(self):
        self.id = 1931
