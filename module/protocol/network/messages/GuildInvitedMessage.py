from module.protocol.network.message import Message


class GuildInvitedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3856
        self.recruterId = {"type": "Number", "value": ""}
        self.recruterName = {"type": "String", "value": ""}
        self.guildInfo = {"type": "BasicGuildInformations", "value": ""}
