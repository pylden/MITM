from module.protocol.network.message import Message


class PartyNewGuestMessage(Message):
    def __init__(self):
        self.id = 2749
