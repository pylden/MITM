from module.protocol.network.messages.NetworkMessage import NetworkMessage


class PurchasableDialogMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6734
        self.buyOrSell = {"type": "Boolean", "value": ""}
        self.purchasableId = {"type": "Number", "value": ""}
        self.purchasableInstanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.price = {"type": "Number", "value": ""}
