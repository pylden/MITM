from module.protocol.network.message import Message


class TrustStatusMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2030
        self.trusted = {"type": "Boolean", "value": ""}
        self.certified = {"type": "Boolean", "value": ""}
