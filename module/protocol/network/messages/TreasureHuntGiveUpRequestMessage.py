from module.protocol.network.message import Message


class TreasureHuntGiveUpRequestMessage(Message):
    def __init__(self):
        self.id = 1127
