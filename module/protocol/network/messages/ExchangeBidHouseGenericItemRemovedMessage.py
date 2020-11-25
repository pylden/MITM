from module.protocol.network.message import Message


class ExchangeBidHouseGenericItemRemovedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8250
        self.objGenericId = {"type": "uint", "value": ""}
