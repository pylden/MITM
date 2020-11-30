from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeCraftPaymentModificationRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6839
        self.quantity = {"type": "Number", "value": ""}
