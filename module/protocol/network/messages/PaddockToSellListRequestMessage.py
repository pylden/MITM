from module.protocol.network.message import Message


class PaddockToSellListRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3095
        self.pageIndex = {"type": "uint", "value": ""}
