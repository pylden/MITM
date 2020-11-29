from module.protocol.network.messages.NetworkMessage import NetworkMessage


class SpouseStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6318
        self.vars.append({"name": "hasSpouse", "type": "Boolean", "value": ""})
