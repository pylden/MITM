from module.protocol.network.message import Message


class GuildInvitationStateRecrutedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4418
        self.invitationState = {"type": "uint", "value": ""}
