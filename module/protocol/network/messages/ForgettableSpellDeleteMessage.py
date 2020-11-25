from module.protocol.network.message import Message


class ForgettableSpellDeleteMessage(Message):
    def __init__(self):
        self.id = 8765
