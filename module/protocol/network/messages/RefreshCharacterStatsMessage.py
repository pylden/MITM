from module.protocol.network.message import Message


class RefreshCharacterStatsMessage(Message):
    def __init__(self):
        self.id = 3914
