from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectRemovedFromBagMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1268
        self.vars.append({"name": "objectUID", "type": "uint", "value": ""})
