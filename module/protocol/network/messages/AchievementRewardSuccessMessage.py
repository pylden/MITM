from module.protocol.network.message import Message


class AchievementRewardSuccessMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5247
        self.achievementId = {"type": "int", "value": ""}
