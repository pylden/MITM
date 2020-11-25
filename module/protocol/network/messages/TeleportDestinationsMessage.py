from module.protocol.network.message import Message


class TeleportDestinationsMessage(Message):
    def __init__(self):
        self.id = 1851
