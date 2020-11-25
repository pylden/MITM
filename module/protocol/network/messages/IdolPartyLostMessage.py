from module.protocol.network.message import Message


class IdolPartyLostMessage(Message):
    def __init__(self):
        self.id = 2578
