from module.protocol.network.message import Message


class PartyJoinMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4142
        self.partyType = {"type": "uint", "value": ""}
        self.partyLeaderId = {"type": "Number", "value": ""}
        self.maxParticipants = {"type": "uint", "value": ""}
        self.members = {"type": "Vector.<PartyMemberInformations>", "value": ""}
        self.guests = {"type": "Vector.<PartyGuestInformations>", "value": ""}
        self.restricted = {"type": "Boolean", "value": ""}
        self.partyName = {"type": "String", "value": ""}
