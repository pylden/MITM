from module.protocol.network.message import Message


class GuildModificationVal2304(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2304
        self.guildName = {"type": "String", "value": ""}
        self.guildEmblem = {"type": "GuildEmblem", "value": ""}
