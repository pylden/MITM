from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightStartingMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6131
        self.fightType = {"type": "uint", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.attackerId = {"type": "Number", "value": ""}
        self.defenderId = {"type": "Number", "value": ""}
        self.containsBoss = {"type": "Boolean", "value": ""}
