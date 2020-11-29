from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GameActionAcknowledgementMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7836
        self.vars.append({"name": "valid", "type": "Boolean", "value": ""})
        self.vars.append({"name": "actionId", "type": "int", "value": ""})
