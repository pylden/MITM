from module.protocol.network.message import Message


class PaddockToSellFilterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1083
        self.areaId = {"type": "int", "value": ""}
        self.atLeastNbMount = {"type": "int", "value": ""}
        self.atLeastNbMachine = {"type": "int", "value": ""}
        self.maxPrice = {"type": "Number", "value": ""}
        self.orderBy = {"type": "uint", "value": ""}
