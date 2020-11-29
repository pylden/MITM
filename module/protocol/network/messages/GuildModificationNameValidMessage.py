from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildModificationNameValidMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 942
        self.vars.append({"name": "guildName", "type": "String", "value": ""})
