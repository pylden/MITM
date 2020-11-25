from module.protocol.network.message import Message


class IdentificationFailedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5865
        self.reason = {"type": "uint", "value": ""}
