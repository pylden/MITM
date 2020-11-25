from module.protocol.network.message import Message


class FriendGuildSetWarnOnAchievementCompleteMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 822
        self.enable = {"type": "Boolean", "value": ""}
