from module.protocol.network.message import Message


class FriendStatusShareStateMessage(Message):
    def __init__(self):
        self.id = 9081
