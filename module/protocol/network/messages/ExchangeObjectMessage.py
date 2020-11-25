from module.protocol.network.message import Message


class ExchangeObjectMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5028
        self.remote = {"type": "Boolean", "value": ""}
