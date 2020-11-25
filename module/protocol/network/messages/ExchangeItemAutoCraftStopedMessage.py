from module.protocol.network.message import Message


class ExchangeItemAutoCraftStopedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2052
        self.reason = {"type": "int", "value": ""}
