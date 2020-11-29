from module.protocol.network.messages.PartyFollowMemberRequestMessage import PartyFollowMemberRequestMessage


class PartyFollowThisMemberRequestMessage(PartyFollowMemberRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        PartyFollowMemberRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4567
        self.vars.append({"name": "enabled", "type": "Boolean", "value": ""})
