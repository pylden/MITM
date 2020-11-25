from module.protocol.network.message import Message


class ExchangeReadyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4086
        self.ready = {"type": "Boolean", "value": ""}
        self.step = {"type": "uint", "value": ""}
