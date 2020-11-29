from module.protocol.network.messages.NetworkMessage import NetworkMessage


class TrustStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2030
        self.vars.append({"name": "trusted", "type": "Boolean", "value": ""})
        self.vars.append({"name": "certified", "type": "Boolean", "value": ""})
