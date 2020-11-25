from module.protocol.network.message import Message


class CharacterSelectedForceMessage(Message):
    def __init__(self):
        self.id = 6332
