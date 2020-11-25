from module.protocol.network.message import Message


class ExchangeBidHouseListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7113
        self.id = {"type": "uint", "value": ""}
        self.follow = {"type": "Boolean", "value": ""}
