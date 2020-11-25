from module.protocol.network.message import Message


class ExchangeBidHouseGenericItemRemovedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8250
        self.objGenericId = {"type": "uint", "value": ""}
