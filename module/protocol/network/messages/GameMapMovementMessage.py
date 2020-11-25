from module.protocol.network.message import Message


class GameMapMovementMessage(Message):
    def __init__(self):
        self.id = 8712
