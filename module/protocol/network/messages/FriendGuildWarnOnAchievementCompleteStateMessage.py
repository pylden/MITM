from module.protocol.network.message import Message


class FriendGuildWarnOnAchievementCompleteStateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 169
        self.enable = {"type": "Boolean", "value": ""}
