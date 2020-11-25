from module.protocol.network.message import Message


class ExchangeWaitingResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5686
        self.bwait = {"type": "Boolean", "value": ""}
