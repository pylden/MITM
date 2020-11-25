from module.protocol.network.message import Message


class ExchangeOkMultiCraftMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6926
        self.initiatorId = {"type": "Number", "value": ""}
        self.otherId = {"type": "Number", "value": ""}
        self.role = {"type": "int", "value": ""}
