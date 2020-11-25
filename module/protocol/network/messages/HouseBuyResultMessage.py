from module.protocol.network.message import Message


class HouseBuyResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6050
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
        self.bought = {"type": "Boolean", "value": ""}
        self.realPrice = {"type": "Number", "value": ""}
