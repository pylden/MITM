from module.protocol.network.messages.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeStartedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4599
        self.vars.append({"name": "firstCharacterId", "type": "Number", "value": ""})
        self.vars.append({"name": "firstCharacterCurrentWeight", "type": "uint", "value": ""})
        self.vars.append({"name": "firstCharacterMaxWeight", "type": "uint", "value": ""})
        self.vars.append({"name": "secondCharacterId", "type": "Number", "value": ""})
        self.vars.append({"name": "secondCharacterCurrentWeight", "type": "uint", "value": ""})
        self.vars.append({"name": "secondCharacterMaxWeight", "type": "uint", "value": ""})
