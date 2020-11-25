from module.protocol.network.message import Message


class FriendUpdateMessage(Message):
    def __init__(self):
        self.id = 9116
