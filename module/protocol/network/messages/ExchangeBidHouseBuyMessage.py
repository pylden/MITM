from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBidHouseBuyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8882
        self.uid = {"type": "uint", "value": ""}
        self.qty = {"type": "uint", "value": ""}
        self.price = {"type": "Number", "value": ""}
