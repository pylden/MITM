from module.protocol.network.message import Message


class ForgettableSpellListUpdateMessage(Message):
    def __init__(self):
        self.id = 1059
