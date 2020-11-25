from module.protocol.network.message import Message


class ExchangeObjectMovePricedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 763
        self.price = {"type": "Number", "value": ""}
