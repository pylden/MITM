from module.protocol.network.message import Message


class GuildCreationVal4933(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4933
        self.guildName = {"type": "String", "value": ""}
        self.guildEmblem = {"type": "GuildEmblem", "value": ""}
