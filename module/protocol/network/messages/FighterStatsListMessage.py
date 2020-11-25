from module.protocol.network.message import Message


class FighterStatsListMessage(Message):
    def __init__(self):
        self.id = 6334
