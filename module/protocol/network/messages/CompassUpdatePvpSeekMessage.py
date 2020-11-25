from module.protocol.network.message import Message


class CompassUpdatePvpSeekMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6287
        self.memberId = {"type": "Number", "value": ""}
        self.memberName = {"type": "String", "value": ""}
