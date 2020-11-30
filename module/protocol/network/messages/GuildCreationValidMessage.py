from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildCreationValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4933
        self.guildName = {"type": "String", "value": ""}
        self.guildEmblem = {"type": "GuildEmblem", "value": ""}
