from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeObjectsRemovedMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5450
        self.vars.append({"name": "objectUID", "type": "Vector.<uint>", "value": ""})
