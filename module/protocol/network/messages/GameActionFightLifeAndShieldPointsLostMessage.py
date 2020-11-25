from module.protocol.network.message import Message


class GameActionFightLifeAndShieldPointsLostMessage(Message):
    def __init__(self):
        self.id = 5065
