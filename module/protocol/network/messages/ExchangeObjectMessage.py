from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeObjectMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5028
        self.vars.append({"name": "remote", "type": "Boolean", "value": ""})
