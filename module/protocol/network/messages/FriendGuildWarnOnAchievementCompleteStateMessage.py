from module.protocol.network.message import Message


class FriendGuildWarnOnAchievementCompleteStateMessage(Message):
    def __init__(self):
        self.id = 169
