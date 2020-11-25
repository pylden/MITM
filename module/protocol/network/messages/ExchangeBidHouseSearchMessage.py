from module.protocol.network.message import Message


class ExchangeBidHouseSearchMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6034
        self.genId = {"type": "uint", "value": ""}
        self.follow = {"type": "Boolean", "value": ""}
