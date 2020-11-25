from module.protocol.network.message import Message


class ExchangeRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5127
        self.exchangeType = {"type": "int", "value": ""}
