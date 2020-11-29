from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightNewRoundMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9076
        self.vars.append({"name": "roundNumber", "type": "uint", "value": ""})
