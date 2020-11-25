from module.protocol.network.message import Message


class PartyJoinMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4142
        self.partyType = {"type": "uint", "value": ""}
        self.partyLeaderId = {"type": "Number", "value": ""}
        self.maxParticipants = {"type": "uint", "value": ""}
        self.members = {"type": "Vector.<PartyMemberInformations>", "value": ""}
        self.guests = {"type": "Vector.<PartyGuestInformations>", "value": ""}
        self.restricted = {"type": "Boolean", "value": ""}
        self.partyName = {"type": "String", "value": ""}
