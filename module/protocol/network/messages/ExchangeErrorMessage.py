from module.protocol.network.message import Message


class ExchangeErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3594
        self.errorType = {"type": "int", "value": ""}
