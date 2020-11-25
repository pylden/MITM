from module.protocol.network.message import Message


class AchievementRewardErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5299
        self.achievementId = {"type": "int", "value": ""}
