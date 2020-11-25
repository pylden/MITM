from module.protocol.network.message import Message


class ChangeThemeRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7258
        self.theme = {"type": "int", "value": ""}
