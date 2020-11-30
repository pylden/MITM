from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PaddockSellBuyDialogMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3281
        self.bsell = {"type": "Boolean", "value": ""}
        self.ownerId = {"type": "uint", "value": ""}
        self.price = {"type": "Number", "value": ""}
