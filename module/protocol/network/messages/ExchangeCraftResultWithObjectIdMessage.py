from module.protocol.network.messages.ExchangeCraftResultMessage import ExchangeCraftResultMessage


class ExchangeCraftResultWithObjectIdMessage(ExchangeCraftResultMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeCraftResultMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9309
        self.objectGenericId = {"type": "uint", "value": ""}
