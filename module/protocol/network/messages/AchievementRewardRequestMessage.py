from module.protocol.network.message import Message


class AchievementRewardRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 368
        self.achievementId = {"type": "int", "value": ""}
