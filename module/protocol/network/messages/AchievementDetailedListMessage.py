from module.protocol.network.message import Message


class AchievementDetailedListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8491
        self.startedAchievements = {"type": "Vector.<Achievement>", "value": ""}
        self.finishedAchievements = {"type": "Vector.<Achievement>", "value": ""}
