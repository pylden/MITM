from module.protocol.network.message import Message


class PartyLeaderUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2432
        self.partyLeaderId = {"type": "Number", "value": ""}
