from module.protocol.network.message import Message


class ExchangeObjectMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5028
        self.remote = {"type": "Boolean", "value": ""}
