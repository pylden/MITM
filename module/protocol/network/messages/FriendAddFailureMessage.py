from module.protocol.network.message import Message


class FriendAddFailureMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5244
        self.reason = {"type": "uint", "value": ""}
