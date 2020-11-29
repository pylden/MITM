from module.protocol.network.messages.IdentificationFailedMessage import IdentificationFailedMessage


class IdentificationFailedForBadVersionMessage(IdentificationFailedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        IdentificationFailedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8091
        self.vars.append({"name": "requiredVersion", "type": "Version", "value": ""})
