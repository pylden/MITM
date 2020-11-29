from module.protocol.network.messages.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerRequestMessage(ExchangeRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 9521
        self.vars.append({"name": "target", "type": "Number", "value": ""})
