from module.protocol.network.message import Message


class HaapiShopApiKeyMessage(Message):
    def __init__(self):
        self.id = 6552
        self.token = {"type": "String", "value": ""}
