from module.protocol.network.message import Message


class CharacterSelectedForceReadyMessage(Message):
    def __init__(self):
        self.id = 765
