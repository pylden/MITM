from module.protocol.network.message import Message


class PrismSettingsErrorMessage(Message):
    def __init__(self):
        self.id = 8894
