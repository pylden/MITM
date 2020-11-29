from module.protocol.network.messages.AllianceListMessage import AllianceListMessage


class AlliancePartialListMessage(AllianceListMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AllianceListMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 71
