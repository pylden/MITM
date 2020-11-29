from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildFactsErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7622
        self.vars.append({"name": "guildId", "type": "uint", "value": ""})
