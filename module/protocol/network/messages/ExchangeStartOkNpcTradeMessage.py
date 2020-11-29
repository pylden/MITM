from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeStartOkNpcTradeMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6982
        self.vars.append({"name": "npcId", "type": "Number", "value": ""})
