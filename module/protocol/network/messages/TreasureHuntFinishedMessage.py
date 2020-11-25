from module.protocol.network.message import Message


class TreasureHuntFinishedMessage(Message):
    def __init__(self):
        self.id = 4291
