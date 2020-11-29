from module.protocol.network.messages.NetworkMessage import NetworkMessage


class FriendGuildWarnOnAchievementCompleteStateMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 169
        self.vars.append({"name": "enable", "type": "Boolean", "value": ""})
