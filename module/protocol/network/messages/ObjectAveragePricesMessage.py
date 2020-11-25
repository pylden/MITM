from module.protocol.network.message import Message


class ObjectAveragePricesMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5825
        self.ids = {"type": "Vector.<uint>", "value": ""}
        self.avgPrices = {"type": "Vector.<Number>", "value": ""}
