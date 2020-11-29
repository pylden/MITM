from module.protocol.network.messages.CompassUpdateMessage import CompassUpdateMessage


class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        CompassUpdateMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7911
        self.vars.append({"name": "memberId", "type": "Number", "value": ""})
        self.vars.append({"name": "active", "type": "Boolean", "value": ""})
