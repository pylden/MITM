from module.protocol.network.message import Message


class CompassUpdatePartyMemberMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7911
        self.memberId = {"type": "Number", "value": ""}
        self.active = {"type": "Boolean", "value": ""}
