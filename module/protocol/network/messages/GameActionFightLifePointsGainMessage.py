from module.protocol.network.message import Message


class GameActionFightLifePointsGainMessage(Message):
    def __init__(self):
        self.id = 5687