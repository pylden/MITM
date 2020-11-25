from module.protocol.network.message import Message


class PartyLoyaltyStatusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4294
        self.loyal = {"type": "Boolean", "value": ""}
