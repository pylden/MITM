from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightNewWaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5791
        self.vars.append({"name": "id", "type": "uint", "value": ""})
        self.vars.append({"name": "teamId", "type": "uint", "value": ""})
        self.vars.append({"name": "nbTurnBeforeNextWave", "type": "int", "value": ""})
