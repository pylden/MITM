from module.protocol.network.message import Message


class HouseSellingUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5119
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.realPrice = {"type": "Number", "value": ""}
        self.buyerName = {"type": "String", "value": ""}
