from module.protocol.network.message import Message


class ExchangeLeaveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 279
        self.success = {"type": "Boolean", "value": ""}
