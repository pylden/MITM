from module.protocol.network.message import Message


class ObjectAveragePricesMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5825
        self.ids = {"type": "Vector.<uint>", "value": ""}
        self.avgPrices = {"type": "Vector.<Number>", "value": ""}
