from module.protocol.network.message import Message


class GuildInvitationMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6688
        self.targetId = {"type": "Number", "value": ""}
