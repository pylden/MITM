from module.protocol.network.message import Message


class IdentificationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5833
        self.version = {"type": "Version", "value": ""}
        self.lang = {"type": "String", "value": ""}
        self.credentials = {"type": "Vector.<int>", "value": ""}
        self.serverId = {"type": "int", "value": ""}
        self.autoconnect = {"type": "Boolean", "value": ""}
        self.useCertificate = {"type": "Boolean", "value": ""}
        self.useLoginToken = {"type": "Boolean", "value": ""}
        self.sessionOptionalSalt = {"type": "Number", "value": ""}
        self.failedAttempts = {"type": "Vector.<uint>", "value": ""}
