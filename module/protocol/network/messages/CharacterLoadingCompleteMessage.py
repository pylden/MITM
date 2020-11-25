from module.protocol.network.message import Message


class CharacterLoadingCompleteMessage(Message):
    def __init__(self):
        self.id = 3354
