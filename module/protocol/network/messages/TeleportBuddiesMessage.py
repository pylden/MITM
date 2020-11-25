from module.protocol.network.message import Message


class TeleportBuddiesMessage(Message):
    def __init__(self):
        self.id = 650
