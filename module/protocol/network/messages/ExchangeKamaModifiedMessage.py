from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangeKamaModifiedMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3838
        self.vars.append({"name": "quantity", "type": "Number", "value": ""})
