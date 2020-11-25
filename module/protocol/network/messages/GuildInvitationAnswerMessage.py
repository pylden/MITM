from module.protocol.network.message import Message


class GuildInvitationAnswerMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8465
        self.accept = {"type": "Boolean", "value": ""}
