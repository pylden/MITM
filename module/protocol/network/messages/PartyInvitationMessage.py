from module.protocol.network.message import Message


class PartyInvitationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4087
        self.partyType = {"type": "uint", "value": ""}
        self.partyName = {"type": "String", "value": ""}
        self.maxParticipants = {"type": "uint", "value": ""}
        self.fromId = {"type": "Number", "value": ""}
        self.fromName = {"type": "String", "value": ""}
        self.toId = {"type": "Number", "value": ""}
