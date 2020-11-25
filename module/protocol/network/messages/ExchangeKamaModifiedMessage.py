from module.protocol.network.message import Message


class ExchangeKamaModifiedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3838
        self.quantity = {"type": "Number", "value": ""}
