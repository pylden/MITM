from module.protocol.network.message import Message


class FriendWarnOnLevelGainStateMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1140
        self.enable = {"type": "Boolean", "value": ""}
