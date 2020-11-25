from module.protocol.network.message import Message


class TeleportBuddiesRequestedMessage(Message):
    def __init__(self):
        self.id = 9376
