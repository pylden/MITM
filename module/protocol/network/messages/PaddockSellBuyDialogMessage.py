from module.protocol.network.message import Message


class PaddockSellBuyDialogMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3281
        self.bsell = {"type": "Boolean", "value": ""}
        self.ownerId = {"type": "uint", "value": ""}
        self.price = {"type": "Number", "value": ""}
