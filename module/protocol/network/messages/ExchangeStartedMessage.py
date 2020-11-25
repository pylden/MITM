from module.protocol.network.message import Message


class ExchangeStartedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 954
        self.exchangeType = {"type": "int", "value": ""}
