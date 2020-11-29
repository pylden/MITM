from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AchievementRewardRequestMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 368
        self.vars.append({"name": "achievementId", "type": "int", "value": ""})
