from module.protocol.network.message import Message


class FriendSetWarnOnLevelGainMessage(Message):
    def __init__(self):
        self.id = 6883
