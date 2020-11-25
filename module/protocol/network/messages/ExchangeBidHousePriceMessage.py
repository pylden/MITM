from module.protocol.network.message import Message


class ExchangeBidHousePriceMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 362
        self.genId = {"type": "uint", "value": ""}
