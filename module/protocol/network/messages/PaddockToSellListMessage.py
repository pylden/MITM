from module.protocol.network.message import Message


class PaddockToSellListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1737
        self.pageIndex = {"type": "uint", "value": ""}
        self.totalPage = {"type": "uint", "value": ""}
        self.paddockList = {"type": "Vector.<PaddockInformationsForSell>", "value": ""}
