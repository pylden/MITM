from module.protocol.network.message import Message


class ExchangeCraftResultWithObjectIdMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9309
        self.objectGenericId = {"type": "uint", "value": ""}
