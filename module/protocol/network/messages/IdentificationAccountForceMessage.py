from module.protocol.network.messages.IdentificationMessage import IdentificationMessage


class IdentificationAccountForceMessage(IdentificationMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        IdentificationMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4388
        self.forcedAccountLogin = {"type": "String", "value": ""}
