from module.protocol.network.message import Message


class GuildMemberOnlineStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6259
        self.memberId = {"type": "Number", "value": ""}
        self.online = {"type": "Boolean", "value": ""}
