from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AchievementRewardErrorMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 5299
        self.achievementId = {"type": "int", "value": ""}
