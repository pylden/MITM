from module.protocol.network.message import Message


class PaddockSellBuyDialogMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3281
        self.bsell = {"type": "Boolean", "value": ""}
        self.ownerId = {"type": "uint", "value": ""}
        self.price = {"type": "Number", "value": ""}
