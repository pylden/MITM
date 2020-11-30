from module.protocol.network.messages.ExchangeStartedMessage import ExchangeStartedMessage


class ExchangeStartedWithPodsMessage(ExchangeStartedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeStartedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4599
        self.firstCharacterId = {"type": "Number", "value": ""}
        self.firstCharacterCurrentWeight = {"type": "uint", "value": ""}
        self.firstCharacterMaxWeight = {"type": "uint", "value": ""}
        self.secondCharacterId = {"type": "Number", "value": ""}
        self.secondCharacterCurrentWeight = {"type": "uint", "value": ""}
        self.secondCharacterMaxWeight = {"type": "uint", "value": ""}
