from module.protocol.network.message import Message


class RefreshCharacterStatsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3914
        self.fighterId = {"type": "Number", "value": ""}
        self.stats = {"type": "GameFightMinimalStats", "value": ""}
