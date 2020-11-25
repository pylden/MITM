from module.protocol.network.message import Message


class GuildInvitationStateRecruterMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 1230
        self.recrutedName = {"type": "String", "value": ""}
        self.invitationState = {"type": "uint", "value": ""}
