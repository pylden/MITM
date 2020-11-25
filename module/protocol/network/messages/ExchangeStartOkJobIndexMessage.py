from module.protocol.network.message import Message


class ExchangeStartOkJobIndexMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 342
        self.jobs = {"type": "Vector.<uint>", "value": ""}
