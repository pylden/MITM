from module.protocol.network.message import Message


class FriendAddRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5946
        self.name = {"type": "String", "value": ""}
