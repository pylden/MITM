from module.protocol.network.message import Message


class ExchangeSellMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 367
        self.objectToSellId = {"type": "uint", "value": ""}
        self.quantity = {"type": "uint", "value": ""}
