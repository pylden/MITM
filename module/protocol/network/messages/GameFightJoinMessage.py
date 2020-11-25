from module.protocol.network.message import Message


class GameFightJoinMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2650
        self.isTeamPhase = {"type": "Boolean", "value": ""}
        self.canBeCancelled = {"type": "Boolean", "value": ""}
        self.canSayReady = {"type": "Boolean", "value": ""}
        self.isFightStarted = {"type": "Boolean", "value": ""}
        self.timeMaxBeforeFightStart = {"type": "uint", "value": ""}
        self.fightType = {"type": "uint", "value": ""}
