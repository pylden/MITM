from module.protocol.network.message import Message


class PurchasableDialogMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6734
        self.buyOrSell = {"type": "Boolean", "value": ""}
        self.purchasableId = {"type": "Number", "value": ""}
        self.purchasableInstanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.price = {"type": "Number", "value": ""}
