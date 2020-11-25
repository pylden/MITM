from module.protocol.network.message import Message


class PartyLoyaltyStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4294
        self.loyal = {"type": "Boolean", "value": ""}
