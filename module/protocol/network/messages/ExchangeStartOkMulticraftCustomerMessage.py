from module.protocol.network.message import Message


class ExchangeStartOkMulticraftCustomerMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1363
        self.skillId = {"type": "uint", "value": ""}
        self.crafterJobLevel = {"type": "uint", "value": ""}
