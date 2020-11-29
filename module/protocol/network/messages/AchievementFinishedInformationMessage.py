from module.protocol.network.messages.AchievementFinishedMessage import AchievementFinishedMessage


class AchievementFinishedInformationMessage(AchievementFinishedMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        AchievementFinishedMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7636
        self.vars.append({"name": "name", "type": "String", "value": ""})
        self.vars.append({"name": "playerId", "type": "Number", "value": ""})
