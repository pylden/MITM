from module.protocol.network.messages.CompassUpdateMessage import CompassUpdateMessage


class CompassUpdatePvpSeekMessage(CompassUpdateMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CompassUpdateMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6287
        self.memberId = {"type": "Number", "value": ""}
        self.memberName = {"type": "String", "value": ""}
