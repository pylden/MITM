from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5763
        self.vars.append({"name": "success", "type": "Boolean", "value": ""})
        self.vars.append({"name": "isFollowed", "type": "Boolean", "value": ""})
        self.vars.append({"name": "followedId", "type": "Number", "value": ""})
