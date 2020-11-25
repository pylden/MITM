from module.protocol.network.message import Message


class ExchangeCraftResultWithObjectIdMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9309
        self.objectGenericId = {"type": "uint", "value": ""}
