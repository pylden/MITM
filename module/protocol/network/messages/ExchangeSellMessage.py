from module.protocol.network.message import Message


class ExchangeSellMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 367
        self.objectToSellId = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
