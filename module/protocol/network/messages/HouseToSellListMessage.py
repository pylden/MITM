from module.protocol.network.message import Message


class HouseToSellListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6887
        self.pageIndex = {"type": "uint", "value": ""}
        self.totalPage = {"type": "uint", "value": ""}
        self.houseList = {"type": "Vector.<HouseInformationsForSell>", "value": ""}
