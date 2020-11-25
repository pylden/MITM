from module.protocol.network.message import Message


class HouseGuildShareRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 429
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.enable = {"type": "Boolean", "value": ""}
        self.rights = {"type": "uint", "value": ""}
