from module.protocol.network.messages.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage


class PartyMemberInBreachFightMessage(AbstractPartyMemberInFightMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMemberInFightMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3143
        self.floor = {"type": "uint", "value": ""}
        self.room = {"type": "uint", "value": ""}
