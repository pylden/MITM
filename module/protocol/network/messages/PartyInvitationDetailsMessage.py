from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationDetailsMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7323
        self.vars.append({"name": "partyType", "type": "uint", "value": ""})
        self.vars.append({"name": "partyName", "type": "String", "value": ""})
        self.vars.append({"name": "fromId", "type": "Number", "value": ""})
        self.vars.append({"name": "fromName", "type": "String", "value": ""})
        self.vars.append({"name": "leaderId", "type": "Number", "value": ""})
        self.vars.append({"name": "members", "type": "Vector.<PartyInvitationMemberInformations>", "value": ""})
        self.vars.append({"name": "guests", "type": "Vector.<PartyGuestInformations>", "value": ""})
