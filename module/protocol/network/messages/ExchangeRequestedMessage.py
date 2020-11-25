from module.protocol.network.message import Message


class ExchangeRequestedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8816
        self.exchangeType = {"type": "int", "value": ""}
