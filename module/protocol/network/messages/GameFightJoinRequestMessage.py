from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightJoinRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3211
        self.vars.append({"name": "fighterId", "type": "Number", "value": ""})
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
