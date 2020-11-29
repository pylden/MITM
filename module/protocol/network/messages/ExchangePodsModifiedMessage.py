from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangePodsModifiedMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7733
        self.vars.append({"name": "currentWeight", "type": "uint", "value": ""})
        self.vars.append({"name": "maxWeight", "type": "uint", "value": ""})
