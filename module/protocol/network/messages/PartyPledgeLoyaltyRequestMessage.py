from module.protocol.network.message import Message


class PartyPledgeLoyaltyRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3196
        self.loyal = {"type": "Boolean", "value": ""}
