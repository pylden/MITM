from module.protocol.network.message import Message


class ExchangeRequestedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8816
        self.exchangeType = {"type": "int", "value": ""}
