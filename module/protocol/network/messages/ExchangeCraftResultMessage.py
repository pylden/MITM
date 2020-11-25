from module.protocol.network.message import Message


class ExchangeCraftResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1988
        self.craftResult = {"type": "uint", "value": ""}
