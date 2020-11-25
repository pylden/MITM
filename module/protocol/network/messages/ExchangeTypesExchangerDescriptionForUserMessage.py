from module.protocol.network.message import Message


class ExchangeTypesExchangerDescriptionForUserMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9562
        self.objectType = {"type": "uint", "value": ""}
        self.typeDescription = {"type": "Vector.<uint>", "value": ""}
