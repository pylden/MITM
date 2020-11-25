from module.protocol.network.message import Message


class FriendGuildWarnOnAchievementCompleteStateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 169
        self.enable = {"type": "Boolean", "value": ""}
