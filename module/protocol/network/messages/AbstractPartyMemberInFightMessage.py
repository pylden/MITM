from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3450
        self.vars.append({"name": "reason", "type": "uint", "value": ""})
        self.vars.append({"name": "memberId", "type": "Number", "value": ""})
        self.vars.append({"name": "memberAccountId", "type": "uint", "value": ""})
        self.vars.append({"name": "memberName", "type": "String", "value": ""})
        self.vars.append({"name": "fightId", "type": "uint", "value": ""})
        self.vars.append({"name": "timeBeforeFightStart", "type": "int", "value": ""})
