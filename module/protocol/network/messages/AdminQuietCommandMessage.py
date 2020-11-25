from module.protocol.network.message import Message


class AdminQuietCommandMessage(Message):
    def __init__(self):
        self.id = 1379
