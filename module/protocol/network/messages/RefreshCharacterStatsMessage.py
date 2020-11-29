from module.protocol.network.messages.NetworkMessage import NetworkMessage


class RefreshCharacterStatsMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3914
        self.vars.append({"name": "fighterId", "type": "Number", "value": ""})
        self.vars.append({"name": "stats", "type": "GameFightMinimalStats", "value": ""})
