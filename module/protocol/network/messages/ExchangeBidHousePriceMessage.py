from module.protocol.network.message import Message


class ExchangeBidHousePriceMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 362
        self.genId = {"type": "uint", "value": ""}
