from module.protocol.network.messages.ExchangeRequestMessage import ExchangeRequestMessage


class ExchangePlayerMultiCraftRequestMessage(ExchangeRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2055
        self.vars.append({"name": "target", "type": "Number", "value": ""})
        self.vars.append({"name": "skillId", "type": "uint", "value": ""})
