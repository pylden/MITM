from module.protocol.network.message import Message


class ChangeThemeRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7258
        self.theme = {"type": "int", "value": ""}
