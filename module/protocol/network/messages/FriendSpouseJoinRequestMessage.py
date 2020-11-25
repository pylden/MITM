from module.protocol.network.message import Message


class FriendSpouseJoinRequestMessage(Message):
    def __init__(self):
        self.id = 9420
