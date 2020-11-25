from module.protocol.network.message import Message


class FriendWarnOnLevelGainStateMessage(Message):
    def __init__(self):
        self.id = 1140
