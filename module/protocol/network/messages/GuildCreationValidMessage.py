from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildCreationValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4933
        self.vars.append({"name": "guildName", "type": "String", "value": ""})
        self.vars.append({"name": "guildEmblem", "type": "GuildEmblem", "value": ""})
