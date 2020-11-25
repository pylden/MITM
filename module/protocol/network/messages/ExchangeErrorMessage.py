from module.protocol.network.message import Message


class ExchangeErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3594
        self.errorType = {"type": "int", "value": ""}
