from module.protocol.network.message import Message


class ServerSettingsMessage(Message):
    def __init__(self):
        self.id = 3435
        self.lang = {"type": "String", "value": ""}
