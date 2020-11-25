from module.protocol.network.message import Message


class ExchangeStartOkMulticraftCrafterMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9643
        self.skillId = {"type": "uint", "value": ""}
