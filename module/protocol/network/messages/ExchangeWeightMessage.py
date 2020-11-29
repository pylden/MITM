from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeWeightMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6558
        self.vars.append({"name": "currentWeight", "type": "uint", "value": ""})
        self.vars.append({"name": "maxWeight", "type": "uint", "value": ""})
