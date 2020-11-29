from module.protocol.network.messages.NetworkMessage import NetworkMessage


class GuildMemberOnlineStatusMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 6259
        self.vars.append({"name": "memberId", "type": "Number", "value": ""})
        self.vars.append({"name": "online", "type": "Boolean", "value": ""})
