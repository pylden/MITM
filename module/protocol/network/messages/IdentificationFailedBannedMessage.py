from module.protocol.network.messages.IdentificationFailedMessage import IdentificationFailedMessage


class IdentificationFailedBannedMessage(IdentificationFailedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        IdentificationFailedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7380
        self.banEndDate = {"type": "Number", "value": ""}
