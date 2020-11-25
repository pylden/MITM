from module.protocol.network.message import Message


class AbstractPartyMemberInFightMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3450
        self.reason = {"type": "uint", "value": ""}
        self.memberId = {"type": "Number", "value": ""}
        self.memberAccountId = {"type": "uint", "value": ""}
        self.memberName = {"type": "String", "value": ""}
        self.fightId = {"type": "uint", "value": ""}
        self.timeBeforeFightStart = {"type": "int", "value": ""}
