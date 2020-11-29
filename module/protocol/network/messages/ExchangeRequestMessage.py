from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5127
        self.vars.append({"name": "exchangeType", "type": "int", "value": ""})
