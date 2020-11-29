from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyJoinMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4142
        self.vars.append({"name": "partyType", "type": "uint", "value": ""})
        self.vars.append({"name": "partyLeaderId", "type": "Number", "value": ""})
        self.vars.append({"name": "maxParticipants", "type": "uint", "value": ""})
        self.vars.append({"name": "members", "type": "Vector.<PartyMemberInformations>", "value": ""})
        self.vars.append({"name": "guests", "type": "Vector.<PartyGuestInformations>", "value": ""})
        self.vars.append({"name": "restricted", "type": "Boolean", "value": ""})
        self.vars.append({"name": "partyName", "type": "String", "value": ""})
