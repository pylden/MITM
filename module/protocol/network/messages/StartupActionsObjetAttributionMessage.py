from module.protocol.network.messages.NetworkMessage import NetworkMessage


class StartupActionsObjetAttributionMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6445
        self.vars.append({"name": "actionId", "type": "uint", "value": ""})
        self.vars.append({"name": "characterId", "type": "Number", "value": ""})
