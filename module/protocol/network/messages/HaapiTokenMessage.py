from module.protocol.network.message import Message


class HaapiTokenMessage(Message):
    def __init__(self):
        self.id = 9546
        self.token = {"type": "String", "value": ""}
