from module.protocol.network.message import Message


class HaapiValidationMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8309
        self.action = {"type": "uint", "value": ""}
        self.code = {"type": "uint", "value": ""}
