from module.protocol.network.message import Message


class PurchasableDialogMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6734
        self.buyOrSell = {"type": "Boolean", "value": ""}
        self.purchasableId = {"type": "Number", "value": ""}
        self.purchasableInstanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.price = {"type": "Number", "value": ""}
