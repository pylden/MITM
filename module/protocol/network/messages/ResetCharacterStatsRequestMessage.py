from module.protocol.network.message import Message


class ResetCharacterStatsRequestMessage(Message):
    def __init__(self):
        self.id = 7291
