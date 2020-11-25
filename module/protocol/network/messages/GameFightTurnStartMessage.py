from module.protocol.network.message import Message


class GameFightTurnStartMessage(Message):
    def __init__(self):
        self.id = 9429
