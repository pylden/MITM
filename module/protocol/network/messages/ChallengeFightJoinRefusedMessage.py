from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ChallengeFightJoinRefusedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7995
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
        self.vars.append({"name": "reason", "type": "int", "value": ""})
