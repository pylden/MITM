from module.protocol.network.message import Message


class GuildInvitationByNameMessage(Message):
    def __init__(self):
        self.id = 4298
        self.name = {"type": "String", "value": ""}
