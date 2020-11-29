from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildJoinedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7966
        self.vars.append({"name": "guildInfo", "type": "GuildInformations", "value": ""})
        self.vars.append({"name": "memberRights", "type": "uint", "value": ""})
