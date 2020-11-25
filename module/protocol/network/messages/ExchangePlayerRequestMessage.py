from module.protocol.network.message import Message


class ExchangePlayerRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9521
        self.target = {"type": "Number", "value": ""}
