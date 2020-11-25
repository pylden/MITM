from module.protocol.network.message import Message


class FriendDeleteResultMessage(Message):
    def __init__(self):
        self.id = 4241
        self.name = {"type": "String", "value": ""}
