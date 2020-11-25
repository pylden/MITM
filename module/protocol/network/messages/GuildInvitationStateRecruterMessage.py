from module.protocol.network.message import Message


class GuildInvitationStateRecruterMessage(Message):
    def __init__(self):
        self.id = 1230
        self.recrutedName = {"type": "String", "value": ""}
