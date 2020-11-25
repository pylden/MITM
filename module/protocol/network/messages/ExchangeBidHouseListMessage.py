from module.protocol.network.message import Message


class ExchangeBidHouseListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7113
        self.id = {"type": "uint", "value": ""}
        self.follow = {"type": "Boolean", "value": ""}
