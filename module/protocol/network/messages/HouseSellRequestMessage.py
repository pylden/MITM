from module.protocol.network.message import Message


class HouseSellRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9737
        self.instanceId = {"type": "uint", "value": ""}
        self.amount = {"type": "Number", "value": ""}
        self.forSale = {"type": "Boolean", "value": ""}
