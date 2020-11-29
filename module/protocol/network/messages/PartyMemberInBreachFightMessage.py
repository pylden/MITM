from module.protocol.network.messages.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage


class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMemberInFightMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3143
        self.vars.append({"name": "floor", "type": "uint", "value": ""})
        self.vars.append({"name": "room", "type": "uint", "value": ""})
