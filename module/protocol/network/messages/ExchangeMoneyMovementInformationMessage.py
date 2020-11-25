from module.protocol.network.message import Message


class ExchangeMoneyMovementInformationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1836
        self.limit = {"type": "Number", "value": ""}
