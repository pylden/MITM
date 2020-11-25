from module.protocol.network.message import Message


class FriendSetStatusShareMessage(Message):
    def __init__(self):
        self.id = 4184
