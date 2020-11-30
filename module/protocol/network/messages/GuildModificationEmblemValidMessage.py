from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildModificationEmblemValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6538
        self.guildEmblem = {"type": "GuildEmblem", "value": ""}
