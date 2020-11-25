from module.protocol.network.message import Message


class PrismFightSwapRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5907
        self.subAreaId = {"type": "uint", "value": ""}
        self.targetId = {"type": "Number", "value": ""}
