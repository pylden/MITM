from module.protocol.network.message import Message


class GameFightJoinMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2650
        self.isTeamPhase = {"type": "Boolean", "value": ""}
        self.canBeCancelled = {"type": "Boolean", "value": ""}
        self.canSayReady = {"type": "Boolean", "value": ""}
        self.isFightStarted = {"type": "Boolean", "value": ""}
        self.timeMaxBeforeFightStart = {"type": "uint", "value": ""}
        self.fightType = {"type": "uint", "value": ""}
