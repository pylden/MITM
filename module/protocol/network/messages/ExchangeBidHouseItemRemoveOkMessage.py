from module.protocol.network.message import Message


class ExchangeBidHouseItemRemoveOkMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8207
        self.sellerId = {"type": "int", "value": ""}
