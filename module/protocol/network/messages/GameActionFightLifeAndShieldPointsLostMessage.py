from module.protocol.network.message import Message


class GameActionFightLifeAndShieldPointsLostMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5065
        self.shieldLoss = {"type": "uint", "value": ""}
