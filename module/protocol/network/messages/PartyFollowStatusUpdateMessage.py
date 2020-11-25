from module.protocol.network.message import Message


class PartyFollowStatusUpdateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5763
        self.success = {"type": "Boolean", "value": ""}
        self.isFollowed = {"type": "Boolean", "value": ""}
        self.followedId = {"type": "Number", "value": ""}
