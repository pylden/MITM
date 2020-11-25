from module.protocol.network.message import Message


class CompassUpdatePartyMemberMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7911
        self.memberId = {"type": "Number", "value": ""}
        self.active = {"type": "Boolean", "value": ""}
