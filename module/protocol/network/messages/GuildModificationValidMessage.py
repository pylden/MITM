from module.protocol.network.message import Message


class GuildModificationValidMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2304
        self.guildName = {"type": "String", "value": ""}
        self.guildEmblem = {"type": "GuildEmblem", "value": ""}
