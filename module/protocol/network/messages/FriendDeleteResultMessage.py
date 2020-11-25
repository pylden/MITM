from module.protocol.network.message import Message


class FriendDeleteResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4241
        self.success = {"type": "Boolean", "value": ""}
        self.name = {"type": "String", "value": ""}
