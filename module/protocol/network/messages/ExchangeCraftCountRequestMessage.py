from module.protocol.network.message import Message


class ExchangeCraftCountRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6588
        self.count = {"type": "int", "value": ""}
