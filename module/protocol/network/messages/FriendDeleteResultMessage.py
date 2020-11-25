from module.protocol.network.message import Message


class FriendDeleteResultMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4241
        self.success = {"type": "Boolean", "value": ""}
        self.name = {"type": "String", "value": ""}
