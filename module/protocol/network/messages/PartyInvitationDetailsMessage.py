from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationDetailsMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7323
        self.partyType = {"type": "uint", "value": ""}
        self.partyName = {"type": "String", "value": ""}
        self.fromId = {"type": "Number", "value": ""}
        self.fromName = {"type": "String", "value": ""}
        self.leaderId = {"type": "Number", "value": ""}
        self.members = {"type": "Vector.<PartyInvitationMemberInformations>", "value": ""}
        self.guests = {"type": "Vector.<PartyGuestInformations>", "value": ""}
