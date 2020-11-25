from module.protocol.network.message import Message


class GameFightTurnResumeMessage(Message):
    def __init__(self):
        self.id = 1375
