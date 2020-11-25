from module.protocol.network.message import Message


class RefreshCharacterStatsMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3914
        self.fighterId = {"type": "Number", "value": ""}
        self.stats = {"type": "GameFightMinimalStats", "value": ""}
