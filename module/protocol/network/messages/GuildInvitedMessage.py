from module.protocol.network.message import Message


class GuildInvitedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3856
        self.recruterId = {"type": "Number", "value": ""}
        self.recruterName = {"type": "String", "value": ""}
        self.guildInfo = {"type": "BasicGuildInformations", "value": ""}
