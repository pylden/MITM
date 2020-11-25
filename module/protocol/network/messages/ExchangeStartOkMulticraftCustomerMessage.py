from module.protocol.network.message import Message


class ExchangeStartOkMulticraftCustomerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1363
        self.skillId = {"type": "uint", "value": ""}
        self.crafterJobLevel = {"type": "uint", "value": ""}
