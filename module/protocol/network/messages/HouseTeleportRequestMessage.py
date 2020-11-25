from module.protocol.network.message import Message


class HouseTeleportRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6194
        self.houseId = {"type": "uint", "value": ""}
        self.houseInstanceId = {"type": "uint", "value": ""}
