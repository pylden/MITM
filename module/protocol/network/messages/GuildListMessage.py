from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 641
        self.vars.append({"name": "guilds", "type": "Vector.<GuildInformations>", "value": ""})
