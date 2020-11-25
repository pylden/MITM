from module.protocol.network.message import Message


class IgnoredDeleteRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7856
        self.accountId = {"type": "uint", "value": ""}
        self.session = {"type": "Boolean", "value": ""}
