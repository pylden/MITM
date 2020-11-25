from module.protocol.network.message import Message


class GuildMemberLeavingMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2202
        self.kicked = {"type": "Boolean", "value": ""}
        self.memberId = {"type": "Number", "value": ""}
