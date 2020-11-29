from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkRecycleTradeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9490
        self.vars.append({"name": "percentToPrism", "type": "uint", "value": ""})
        self.vars.append({"name": "percentToPlayer", "type": "uint", "value": ""})
