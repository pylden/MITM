from module.protocol.network.message import Message


class FriendDeleteRequestMessage(Message):
    def __init__(self):
        self.id = 3469
