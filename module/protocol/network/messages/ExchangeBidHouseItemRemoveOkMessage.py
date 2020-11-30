from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseItemRemoveOkMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8207
        self.sellerId = {"type": "int", "value": ""}
