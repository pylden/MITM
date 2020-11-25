from module.protocol.network.message import Message


class CompassUpdatePvpSeekMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6287
        self.memberId = {"type": "Number", "value": ""}
        self.memberName = {"type": "String", "value": ""}
