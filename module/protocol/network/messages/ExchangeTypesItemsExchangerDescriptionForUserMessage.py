from module.protocol.network.message import Message


class ExchangeTypesItemsExchangerDescriptionForUserMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8949
        self.objectType = {"type": "uint", "value": ""}
        self.itemTypeDescriptions = {"type": "Vector.<BidExchangerObjectInfo>", "value": ""}
