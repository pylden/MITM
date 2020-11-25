from module.protocol.network.message import Message


class PartyLeaderUpdateMessage(Message):
    def __init__(self):
        self.id = 2432
