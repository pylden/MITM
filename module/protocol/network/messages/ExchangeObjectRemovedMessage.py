from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectRemovedMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1377
        self.objectUID = {"type": "uint", "value": ""}
