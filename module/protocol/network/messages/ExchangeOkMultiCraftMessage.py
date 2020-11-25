from module.protocol.network.message import Message


class ExchangeOkMultiCraftMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6926
        self.initiatorId = {"type": "Number", "value": ""}
        self.otherId = {"type": "Number", "value": ""}
        self.role = {"type": "int", "value": ""}
