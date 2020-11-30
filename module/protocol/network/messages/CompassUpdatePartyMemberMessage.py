from module.protocol.network.messages.CompassUpdateMessage import CompassUpdateMessage


class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CompassUpdateMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7911
        self.memberId = {"type": "Number", "value": ""}
        self.active = {"type": "Boolean", "value": ""}
