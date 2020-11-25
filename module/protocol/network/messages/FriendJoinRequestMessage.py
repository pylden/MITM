from module.protocol.network.message import Message


class FriendJoinRequestMessage(Message):
    def __init__(self):
        self.id = 4174
        self.name = {"type": "String", "value": ""}
