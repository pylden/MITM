from module.protocol.network.message import Message


class AchievementDetailedListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8491
        self.startedAchievements = {"type": "Vector.<Achievement>", "value": ""}
        self.finishedAchievements = {"type": "Vector.<Achievement>", "value": ""}
