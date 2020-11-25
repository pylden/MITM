from module.protocol.network.message import Message


class ExchangeMoneyMovementInformationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1836
        self.limit = {"type": "Number", "value": ""}
