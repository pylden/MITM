from module.protocol.network.message import Message


class PartyRestrictedMessage(Message):
    def __init__(self):
        self.id = 2491
