from module.protocol.network.messages.NetworkMessage import NetworkMessage


class BasicStatMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9271
        self.vars.append({"name": "timeSpent", "type": "Number", "value": ""})
        self.vars.append({"name": "statId", "type": "uint", "value": ""})
