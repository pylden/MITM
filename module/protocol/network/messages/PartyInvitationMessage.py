from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyInvitationMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4087
        self.vars.append({"name": "partyType", "type": "uint", "value": ""})
        self.vars.append({"name": "partyName", "type": "String", "value": ""})
        self.vars.append({"name": "maxParticipants", "type": "uint", "value": ""})
        self.vars.append({"name": "fromId", "type": "Number", "value": ""})
        self.vars.append({"name": "fromName", "type": "String", "value": ""})
        self.vars.append({"name": "toId", "type": "Number", "value": ""})
