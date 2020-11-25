from module.protocol.network.message import Message


class HelloConnectMessage(Message):
    def __init__(self):
        self.id = 2607
        self.salt = {"type": "String", "value": ""}
