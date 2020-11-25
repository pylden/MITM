from module.protocol.network.message import Message


class HouseSellingUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5119
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.realPrice = {"type": "Number", "value": ""}
        self.buyerName = {"type": "String", "value": ""}
