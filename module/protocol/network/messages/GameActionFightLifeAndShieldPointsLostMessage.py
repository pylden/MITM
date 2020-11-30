from module.protocol.network.messages.GameActionFightLifePointsLostMessage import GameActionFightLifePointsLostMessage


class GameActionFightLifeAndShieldPointsLostMessage(GameActionFightLifePointsLostMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameActionFightLifePointsLostMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5065
        self.shieldLoss = {"type": "uint", "value": ""}
