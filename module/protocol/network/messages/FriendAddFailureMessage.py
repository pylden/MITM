from module.protocol.network.message import Message


class FriendAddFailureMessage(Message):
    def __init__(self):
        self.id = 5244
