from module.protocol.network.message import Message


class AchievementFinishedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2350
        self.achievement = {"type": "AchievementAchievedRewardable", "value": ""}
