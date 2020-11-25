from module.protocol.network.message import Message


class FriendSpouseFollowWithCompassRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 560
        self.enable = {"type": "Boolean", "value": ""}
