from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightNewWaveMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5791
        self.id = {"type": "uint", "value": ""}
        self.teamId = {"type": "uint", "value": ""}
        self.nbTurnBeforeNextWave = {"type": "int", "value": ""}
