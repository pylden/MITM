from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightJoinMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2650
        self.vars.append({"name": "isTeamPhase", "type": "Boolean", "value": ""})
        self.vars.append({"name": "canBeCancelled", "type": "Boolean", "value": ""})
        self.vars.append({"name": "canSayReady", "type": "Boolean", "value": ""})
        self.vars.append({"name": "isFightStarted", "type": "Boolean", "value": ""})
        self.vars.append({"name": "timeMaxBeforeFightStart", "type": "uint", "value": ""})
        self.vars.append({"name": "fightType", "type": "uint", "value": ""})
