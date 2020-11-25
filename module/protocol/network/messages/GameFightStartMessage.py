from module.protocol.network.message import Message


class GameFightStartMessage(Message):
    def __init__(self):
        self.id = 9280
