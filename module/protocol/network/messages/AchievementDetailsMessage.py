from module.protocol.network.message import Message


class AchievementDetailsMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 360
        self.achievement = {"type": "Achievement", "value": ""}
