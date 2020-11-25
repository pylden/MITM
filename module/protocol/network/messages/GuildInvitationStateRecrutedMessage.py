from module.protocol.network.message import Message


class GuildInvitationStateRecrutedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4418
        self.invitationState = {"type": "uint", "value": ""}
