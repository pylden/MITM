from module.protocol.network.message import Message


class ExchangeStoppedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6266
        self.id = {"type": "Number", "value": ""}
