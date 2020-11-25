from module.protocol.network.message import Message


class AchievementRewardErrorMessage(Message):
    def __init__(self):
        self.id = 5299
