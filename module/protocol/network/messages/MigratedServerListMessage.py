from module.protocol.network.message import Message


class MigratedServerListMessage(Message):
    def __init__(self):
        self.id = 5457
