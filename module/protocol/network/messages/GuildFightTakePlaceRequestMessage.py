from module.protocol.network.messages.GuildFightJoinRequestMessage import GuildFightJoinRequestMessage


class GuildFightTakePlaceRequestMessage(GuildFightJoinRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GuildFightJoinRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8763
        self.replacedCharacterId = {"type": "int", "value": ""}
