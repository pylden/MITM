from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameFightHumanReadyStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 386
        self.vars.append({"name": "characterId", "type": "Number", "value": ""})
        self.vars.append({"name": "isReady", "type": "Boolean", "value": ""})
