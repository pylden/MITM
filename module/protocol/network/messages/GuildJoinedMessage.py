from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildJoinedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7966
        self.guildInfo = {"type": "GuildInformations", "value": ""}
        self.memberRights = {"type": "uint", "value": ""}
