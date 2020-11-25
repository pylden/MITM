from module.protocol.network.message import Message


class FriendWarnOnConnectionStateMessage(Message):
    def __init__(self):
        self.id = 8749
