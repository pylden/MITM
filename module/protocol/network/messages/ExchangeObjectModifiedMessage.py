from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectModifiedMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6307
        self.vars.append({"name": "object", "type": "ObjectItem", "value": ""})
