from module.protocol.network.message import Message


class PartyFollowStatusUpdateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5763
        self.success = {"type": "Boolean", "value": ""}
        self.isFollowed = {"type": "Boolean", "value": ""}
        self.followedId = {"type": "Number", "value": ""}
