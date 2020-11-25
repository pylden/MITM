from module.protocol.network.message import Message


class HouseToSellFilterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9720
        self.areaId = {"type": "int", "value": ""}
        self.atLeastNbRoom = {"type": "uint", "value": ""}
        self.atLeastNbChest = {"type": "uint", "value": ""}
        self.skillRequested = {"type": "uint", "value": ""}
        self.maxPrice = {"type": "Number", "value": ""}
        self.orderBy = {"type": "uint", "value": ""}
