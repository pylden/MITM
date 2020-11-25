from module.protocol.network.message import Message


class GameActionSpamMessage(Message):
    def __init__(self):
        self.id = 1035
