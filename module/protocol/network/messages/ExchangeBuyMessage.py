from module.protocol.network.messages.NetworkMessage import NetworkMessage


class ExchangeBuyMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4224
        self.objectToBuyId = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
