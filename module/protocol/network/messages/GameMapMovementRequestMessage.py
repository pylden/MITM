from module.protocol.network.message import Message


class GameMapMovementRequestMessage(Message):
    def __init__(self):
        self.id = 7064
