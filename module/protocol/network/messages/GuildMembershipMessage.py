from module.protocol.network.messages.GuildJoinedMessage import GuildJoinedMessage


class GuildMembershipMessage(GuildJoinedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GuildJoinedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1467
