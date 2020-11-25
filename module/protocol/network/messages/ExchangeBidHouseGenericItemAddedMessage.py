from module.protocol.network.message import Message


class ExchangeBidHouseGenericItemAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1178
        self.objGenericId = {"type": "uint", "value": ""}
