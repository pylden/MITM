from module.protocol.network.message import Message


class GameFightPauseMessage(Message):
    def __init__(self):
        self.id = 6766
