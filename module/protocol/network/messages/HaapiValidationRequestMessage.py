from module.protocol.network.message import Message


class HaapiValidationRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9199
        self.transaction = {"type": "String", "value": ""}
