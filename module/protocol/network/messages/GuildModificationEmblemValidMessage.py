from module.protocol.network.message import Message


class GuildModificationEmblemVal6538(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6538
        self.guildEmblem = {"type": "GuildEmblem", "value": ""}
