from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeSellMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 367
        self.objectToSellId = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
