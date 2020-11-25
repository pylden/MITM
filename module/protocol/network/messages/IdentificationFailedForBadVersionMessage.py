from module.protocol.network.message import Message


class IdentificationFailedForBadVersionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8091
        self.requiredVersion = {"type": "Version", "value": ""}
