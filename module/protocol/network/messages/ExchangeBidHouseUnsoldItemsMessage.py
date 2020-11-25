from module.protocol.network.message import Message


class ExchangeBidHouseUnsoldItemsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5367
        self.items = {"type": "Vector.<ObjectItemGenericQuantity>", "value": ""}
