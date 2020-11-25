from module.protocol.network.message import Message


class FriendWarnOnConnectionStateMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8749
        self.enable = {"type": "Boolean", "value": ""}
