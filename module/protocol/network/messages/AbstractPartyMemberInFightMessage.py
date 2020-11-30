from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class AbstractPartyMemberInFightMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3450
        self.reason = {"type": "uint", "value": ""}
        self.memberId = {"type": "Number", "value": ""}
        self.memberAccountId = {"type": "uint", "value": ""}
        self.memberName = {"type": "String", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.timeBeforeFightStart = {"type": "int", "value": ""}
