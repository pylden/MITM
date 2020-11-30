from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AchievementListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 3550
        self.finishedAchievements = {"type": "Vector.<AchievementAchieved>", "value": ""}
