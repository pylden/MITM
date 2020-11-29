from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightTurnReadyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 983
        self.vars.append({"name": "isReady", "type": "Boolean", "value": ""})
