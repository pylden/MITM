from module.protocol.network.message import Message


class GuildMemberSetWarnOnConnectionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9973
        self.enable = {"type": "Boolean", "value": ""}
