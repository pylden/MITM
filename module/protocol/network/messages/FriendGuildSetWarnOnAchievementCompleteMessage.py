from module.protocol.network.message import Message


class FriendGuildSetWarnOnAchievementCompleteMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 822
        self.enable = {"type": "Boolean", "value": ""}
