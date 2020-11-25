from module.protocol.network.message import Message


class ExchangeTypesExchangerDescriptionForUserMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9562
        self.objectType = {"type": "uint", "value": ""}
        self.typeDescription = {"type": "Vector.<uint>", "value": ""}
