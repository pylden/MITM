from module.protocol.network.message import Message


class TeleportHavenBagRequestMessage(Message):
    def __init__(self):
        self.id = 8318
