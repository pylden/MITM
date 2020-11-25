from module.protocol.network.message import Message


class GuildFightTakePlaceRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8763
        self.replacedCharacterId = {"type": "int", "value": ""}
