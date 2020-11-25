from module.protocol.network.message import Message


class GameActionFightLifePointsLostMessage(Message):
    def __init__(self):
        self.id = 2479
