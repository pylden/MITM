from module.protocol.network.message import Message


class TeleportRequestMessage(Message):
    def __init__(self):
        self.id = 1080
