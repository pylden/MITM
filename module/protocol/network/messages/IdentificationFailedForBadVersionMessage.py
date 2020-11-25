from module.protocol.network.message import Message


class IdentificationFailedForBadVersionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8091
        self.requiredVersion = {"type": "Version", "value": ""}
