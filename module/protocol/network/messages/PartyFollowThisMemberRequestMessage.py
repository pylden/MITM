from module.protocol.network.message import Message


class PartyFollowThisMemberRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4567
        self.enabled = {"type": "Boolean", "value": ""}
