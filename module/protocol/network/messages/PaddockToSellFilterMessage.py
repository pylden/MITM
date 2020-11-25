from module.protocol.network.message import Message


class PaddockToSellFilterMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1083
        self.areaId = {"type": "int", "value": ""}
        self.atLeastNbMount = {"type": "int", "value": ""}
        self.atLeastNbMachine = {"type": "int", "value": ""}
        self.maxPrice = {"type": "Number", "value": ""}
        self.orderBy = {"type": "uint", "value": ""}
