from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AchievementFinishedMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 2350
        self.vars.append({"name": "achievement", "type": "AchievementAchievedRewardable", "value": ""})
