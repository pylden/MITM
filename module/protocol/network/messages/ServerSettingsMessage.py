from module.protocol.network.message import Message


class ServerSettingsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3435
        self.lang = {"type": "String", "value": ""}
