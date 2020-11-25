from module.protocol.network.message import Message


class ChangeThemeRequestMessage(Message):
    def __init__(self):
        self.id = 7258
