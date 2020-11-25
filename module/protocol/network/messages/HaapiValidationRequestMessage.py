from module.protocol.network.message import Message


class HaapiValidationRequestMessage(Message):
    def __init__(self):
        self.id = 9199
        self.transaction = {"type": "String", "value": ""}
