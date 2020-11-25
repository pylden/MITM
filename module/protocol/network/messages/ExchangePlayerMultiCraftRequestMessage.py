from module.protocol.network.message import Message


class ExchangePlayerMultiCraftRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2055
        self.target = {"type": "Number", "value": ""}
        self.skillId = {"type": "uint", "value": ""}
