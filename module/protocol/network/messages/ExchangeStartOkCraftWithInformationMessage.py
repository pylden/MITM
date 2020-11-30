from module.protocol.network.messages.ExchangeStartOkCraftMessage import ExchangeStartOkCraftMessage


class ExchangeStartOkCraftWithInformationMessage(ExchangeStartOkCraftMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeStartOkCraftMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7187
        self.skillId = {"type": "uint", "value": ""}
