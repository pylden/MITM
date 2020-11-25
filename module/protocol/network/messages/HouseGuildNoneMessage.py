from module.protocol.network.message import Message


class HouseGuildNoneMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8272
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.secondHand = {"type": "Boolean", "value": ""}
