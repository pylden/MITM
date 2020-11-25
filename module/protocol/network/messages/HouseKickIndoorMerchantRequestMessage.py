from module.protocol.network.message import Message


class HouseKickIndoorMerchantRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6829
        self.cellId = {"type": "uint", "value": ""}
