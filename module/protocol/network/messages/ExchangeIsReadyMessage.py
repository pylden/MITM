from module.protocol.network.message import Message


class ExchangeIsReadyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2446
        self.id = {"type": "Number", "value": ""}
        self.ready = {"type": "Boolean", "value": ""}
