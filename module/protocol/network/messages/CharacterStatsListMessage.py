from module.protocol.network.message import Message


class CharacterStatsListMessage(Message):
    def __init__(self):
        self.id = 8872
