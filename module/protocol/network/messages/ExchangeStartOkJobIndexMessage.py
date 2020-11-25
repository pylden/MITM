from module.protocol.network.message import Message


class ExchangeStartOkJobIndexMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 342
        self.jobs = {"type": "Vector.<uint>", "value": ""}
