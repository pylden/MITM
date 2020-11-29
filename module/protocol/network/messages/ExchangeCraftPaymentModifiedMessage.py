from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftPaymentModifiedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1491
        self.vars.append({"name": "goldSum", "type": "Number", "value": ""})
