from module.protocol.network.messages.AbstractPartyMessage import AbstractPartyMessage


class PartyFollowStatusUpdateMessage(AbstractPartyMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AbstractPartyMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5763
        self.success = {"type": "Boolean", "value": ""}
        self.isFollowed = {"type": "Boolean", "value": ""}
        self.followedId = {"type": "Number", "value": ""}
