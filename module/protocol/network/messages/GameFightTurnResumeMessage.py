from module.protocol.network.messages.GameFightTurnStartMessage import GameFightTurnStartMessage


class GameFightTurnResumeMessage(GameFightTurnStartMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameFightTurnStartMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1375
        self.remainingTime = {"type": "uint", "value": ""}
