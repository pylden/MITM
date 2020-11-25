from module.protocol.network.message import Message


class NumericWhoIsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9545
        self.playerId = {"type": "Number", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
