from module.protocol.network.message import Message


class PartyLeaderUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2432
        self.partyLeaderId = {"type": "Number", "value": ""}
