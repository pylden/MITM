from module.protocol.network.message import Message


class HaapiApiKeyMessage(Message):
    def __init__(self):
        self.id = 1489
        self.token = {"type": "String", "value": ""}
