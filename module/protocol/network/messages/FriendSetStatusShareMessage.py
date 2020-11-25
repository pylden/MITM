from module.protocol.network.message import Message


class FriendSetStatusShareMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4184
        self.share = {"type": "Boolean", "value": ""}
