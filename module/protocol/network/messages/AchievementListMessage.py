from module.protocol.network.message import Message


class AchievementListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3550
        self.finishedAchievements = {"type": "Vector.<AchievementAchieved>", "value": ""}
