from module.protocol.network.message import Message


class PartyInvitationDetailsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7323
        self.partyType = {"type": "uint", "value": ""}
        self.partyName = {"type": "String", "value": ""}
        self.fromId = {"type": "Number", "value": ""}
        self.fromName = {"type": "String", "value": ""}
        self.leaderId = {"type": "Number", "value": ""}
        self.members = {"type": "Vector.<PartyInvitationMemberInformations>", "value": ""}
        self.guests = {"type": "Vector.<PartyGuestInformations>", "value": ""}
