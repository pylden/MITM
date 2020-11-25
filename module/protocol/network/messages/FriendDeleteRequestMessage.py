from module.protocol.network.message import Message


class FriendDeleteRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3469
        self.accountId = {"type": "uint", "value": ""}
