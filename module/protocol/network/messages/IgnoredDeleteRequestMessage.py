from module.protocol.network.messages.NetworkMessage import NetworkMessage


class IgnoredDeleteRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7856
        self.vars.append({"name": "accountId", "type": "uint", "value": ""})
        self.vars.append({"name": "session", "type": "Boolean", "value": ""})
