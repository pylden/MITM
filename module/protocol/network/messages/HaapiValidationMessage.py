from module.protocol.network.message import Message


class HaapiValidationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8309
        self.action = {"type": "uint", "value": ""}
        self.code = {"type": "uint", "value": ""}
