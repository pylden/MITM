from module.protocol.network.message import Message


class HouseSellRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9737
        self.instanceId = {"type": "uint", "value": ""}
        self.amount = {"type": "Number", "value": ""}
        self.forSale = {"type": "Boolean", "value": ""}
