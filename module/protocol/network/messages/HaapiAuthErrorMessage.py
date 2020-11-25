from module.protocol.network.message import Message


class HaapiAuthErrorMessage(Message):
    def __init__(self):
        self.id = 1617
