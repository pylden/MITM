from module.protocol.network.message import Message


class FriendAddRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5946
        self.name = {"type": "String", "value": ""}
