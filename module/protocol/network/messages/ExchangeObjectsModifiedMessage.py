from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectsModifiedMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 363
        self.vars.append({"name": "object", "type": "Vector.<ObjectItem>", "value": ""})
