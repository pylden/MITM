from module.protocol.network.message import Message


class TeleportToBuddyOfferMessage(Message):
    def __init__(self):
        self.id = 5460
