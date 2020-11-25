from module.protocol.network.message import Message


class AchievementFinishedMessage(Message):
    def __init__(self):
        self.id = 2350
