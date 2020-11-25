from module.protocol.network.message import Message


class AchievementDetailsRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1661
        self.achievementId = {"type": "uint", "value": ""}
