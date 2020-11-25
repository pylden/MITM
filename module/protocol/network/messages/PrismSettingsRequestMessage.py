from module.protocol.network.message import Message


class PrismSettingsRequestMessage(Message):
    def __init__(self):
        self.id = 8733
