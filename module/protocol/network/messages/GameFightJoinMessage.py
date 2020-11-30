from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightJoinMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2650
        self.isTeamPhase = {"type": "Boolean", "value": ""}
        self.canBeCancelled = {"type": "Boolean", "value": ""}
        self.canSayReady = {"type": "Boolean", "value": ""}
        self.isFightStarted = {"type": "Boolean", "value": ""}
        self.timeMaxBeforeFightStart = {"type": "uint", "value": ""}
        self.fightType = {"type": "uint", "value": ""}
