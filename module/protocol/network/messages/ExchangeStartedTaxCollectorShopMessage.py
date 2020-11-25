from module.protocol.network.message import Message


class ExchangeStartedTaxCollectorShopMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8259
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
        self.kamas = {"type": "Number", "value": ""}
