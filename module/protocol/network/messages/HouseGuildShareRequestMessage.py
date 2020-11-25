from module.protocol.network.message import Message


class HouseGuildShareRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 429
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
        self.enable = {"type": "Boolean", "value": ""}
        self.rights = {"type": "uint", "value": ""}
