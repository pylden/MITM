from module.protocol.network.message import Message


class AchievementRewardRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 368
        self.achievementId = {"type": "int", "value": ""}
