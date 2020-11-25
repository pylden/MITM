from module.protocol.network.message import Message


class PaddockToSellListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1737
        self.pageIndex = {"type": "uint", "value": ""}
        self.totalPage = {"type": "uint", "value": ""}
        self.paddockList = {"type": "Vector.<PaddockInformationsForSell>", "value": ""}
