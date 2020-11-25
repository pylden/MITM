from module.protocol.network.message import Message


class GameFightEndMessage(Message):
    def __init__(self):
        self.id = 1090
