from module.protocol.network.message import Message


class GuildCreationValidMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4933
        self.guildName = {"type": "String", "value": ""}
        self.guildEmblem = {"type": "GuildEmblem", "value": ""}
