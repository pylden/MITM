from module.protocol.network.message import Message


class FriendAddRequestMessage(Message):
    def __init__(self):
        self.id = 5946
        self.name = {"type": "String", "value": ""}
