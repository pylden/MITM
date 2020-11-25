from module.protocol.network.message import Message


class ExchangeWeightMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6558
        self.currentWeight = {"type": "uint", "value": ""}
        self.maxWeight = {"type": "uint", "value": ""}
