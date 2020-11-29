from module.protocol.network.messages.NetworkMessage import NetworkMessage


class AchievementDetailedListMessage(NetworkMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NetworkMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 8491
        self.vars.append({"name": "startedAchievements", "type": "Vector.<Achievement>", "value": ""})
        self.vars.append({"name": "finishedAchievements", "type": "Vector.<Achievement>", "value": ""})
