from module.protocol.network.message import Message


class GuildInvitationStateRecruterMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1230
        self.recrutedName = {"type": "String", "value": ""}
