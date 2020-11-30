from module.protocol.network.messages.ExchangeObjectMessage import ExchangeObjectMessage


class ExchangePodsModifiedMessage(ExchangeObjectMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ExchangeObjectMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7733
        self.currentWeight = {"type": "uint", "value": ""}
        self.maxWeight = {"type": "uint", "value": ""}
