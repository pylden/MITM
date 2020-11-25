from module.protocol.network.message import Message


class HaapiSessionMessage(Message):
    def __init__(self):
        self.id = 6833
        self.key = {"type": "String", "value": ""}
