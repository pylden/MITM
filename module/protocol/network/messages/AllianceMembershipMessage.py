from module.protocol.network.messages.AllianceJoinedMessage import AllianceJoinedMessage


class AllianceMembershipMessage(AllianceJoinedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AllianceJoinedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7070
