from module.protocol.network.message import Message


class HouseGuildRightsViewMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2589
        self.houseId = {"type": "uint", "value": ""}
        self.instanceId = {"type": "uint", "value": ""}
