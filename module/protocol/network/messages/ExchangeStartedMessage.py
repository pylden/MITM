from module.protocol.network.message import Message


class ExchangeStartedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 954
        self.exchangeType = {"type": "int", "value": ""}
