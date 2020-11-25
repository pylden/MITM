from module.protocol.network.message import Message


class ExchangeStartOkCraftWithInformationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7187
        self.skillId = {"type": "uint", "value": ""}
